# 多層 NNPF 読解例：同じ時刻の別レイヤーを、過去フレームと取り違えない

[NNPF読書案内](nnpf-reading.md) / [AR寄書との対応](nnpf-ar-reading-map.md)

確認基準日：2026年10月4日。

## 確認版・範囲

対象は **JVET-AQ0053-v2「AHG9: On multilayer NNPF」**。個別寄書の提案であり、承認済み規格そのものではない。比較先は JVET-AQ2032 の配布 v4 ZIP に入っている **`JVET-AQ2032-v3.docx`**（TuC）。配布版と内部ファイル名を区別する。[7][14]

AQ0053 §1.2–§2.3 と、AQ2032 の **「NNPF multilayer support option 2: Modify VVC clause D.12.11 per JVET-AJ0130 and JVET-AQ0053」** 本文を照合した。以下のページは DOCX を LibreOffice で PDF 化した際の印刷ページ番号（AQ0053 pp.1–5、比較先の該当箇所 pp.42–44）。AQ0053 pp.2–5、AQ2032 pp.43–44 は描画を目視確認し、変更履歴は DOCX 内 `word/document.xml` とも照合した。TuC の収録リストだけからの推定ではない。[7][14]

**図と数値は説明用に作った読解例であり、寄書の実験結果・実装・適合ビットストリームではない。** 実 decoder による sub-bitstream extraction や推論の実験はしていない。

## 1. まず「入力2枚」の軸を分ける

NNPFC はフィルターの特性、NNPFA はその activation を読む入口になる。本例では NNPFC の `nnpfc_id` と NNPFA の `nnpfa_target_id` を同じ値にする。関連 NNPFC 自体を scalable nesting の中に入れることは必須ではない（AQ0053 §2.3, D.12.11.3, p.4）。[7]

AQ0053 §1.2（p.1）は、従来の VVC interface では複数入力を **現在の CLVS 内で、現在 picture から逆 output order** に選ぶ一方、AJ0130 由来の多層案では scalable-nested NNPFA により **同じ AU の指定レイヤー群**から選ぶ、と整理している。枚数だけではどちらの意味か決まらない。[7]

### 説明用の設定

- レイヤー `L0`（`nuh_layer_id = 0`）と `L1`（`nuh_layer_id = 1`）。たとえば2視点の映像を想定するが、視点合成・補助レイヤーなど用途は別途決める。
- `NestingNumLayers = 2`、導出済み `NestingLayerId[ 0 ] = 0`、`NestingLayerId[ 1 ] = 1` と仮定する。配列導出そのものはここでは再実装しない。
- `nnpfc_num_input_pics_minus1 = 1`、従って `numInputPics = 2`。
- 対象 NNPFA は active、`sn_ols_flag = 0`、`sn_subpic_flag = 0` の scalable nesting 内にある。
- 各 AU に両レイヤーの picture が存在し、ともに `PictureOutputFlag = 1`。各入力の conformance window 適用後の幅・高さを同じ `1920 × 1080`、picture の `BitDepth` をともに `10` と仮定する（bit-depth 文言の留保は後述）。

これらは以下の D.12.11.3 を追うための設定であって、実際の SPS/PPS・NN モデル・出力先の仕様を全部与えたものではない。

```text
横軸：output order に沿う時刻（この図では各列が1 AU）
                     AU(t−1)             AU(t)             AU(t+1)
L1 / layer_id=1       B(t−1)              B(t)               B(t+1)
                                          │ 入力スロット1
                                          ▼
                                    [ 多層 NNPF ]
                                          ▲
                                          │ 入力スロット0
L0 / layer_id=0       A(t−1)              A(t)               A(t+1)

意図した AU(t) の入力： [ A(t), B(t) ]  ← 同じ列、別レイヤー
時間方向の2枚入力：    [ A(t), A(t−1) ] ← 同じ行、別時刻
```

この図の「縦」はレイヤー間の入力選択であって、符号化予測依存や物理的 NAL 配置の順序ではない。同じ AU の `NestingLayerId[i]` の picture を `CroppedYPic[i]` に割り当てる規則が根拠である（AQ0053 §2.3, D.12.11.3, pp.4–5）。[7]

## 2. extraction で何が壊れるのか

AQ0053 §1.3（p.2）は VVC の general sub-bitstream extraction の手順 9(c) を引用している。特に、対象 OLS が1レイヤーで、`sn_ols_flag = 0`、`sn_subpic_flag = 0` の scalable nesting が残るレイヤーに適用される場合、内側の SEI を新しい SEI NAL unit に **non-scalable-nested として直接入れ**、元の外側の SEI NAL unit を除去する。単に picture を削るだけではない。[7]

```text
抽出前：2層を含む入力
  scalable nesting（対象 L0, L1）
    └─ NNPFA（2枚入力の NNPF を activate）
  AU(t): A(t), B(t)
              │
              │ L0 だけの OLS へ抽出（上記条件）
              ▼
抽出後：L0 の sub-bitstream
  NNPFA（外側の nesting がなく、直接置かれる）
  AU(t): A(t)          B(t) は残らない
```

**問題は入力が1枚減ることに加え、activation の見え方が変わること。** Cross-layer の区別を持たない読み方では、non-nested NNPFA に対して通常の時間方向の選択を行ってしまう。十分な過去の output picture があるという本例の仮定なら、期待した `[A(t), B(t)]` が `[A(t), A(t−1)]` になる。枚数は2枚のままでも、モデルに渡す意味が違う。これは寄書が指摘する失敗を図にしたもので、全ての抽出・全ての実装で必ず再現すると主張するものではない（§1.2–§1.3）。[7]

## 3. `0x400` は入力を増やす指定ではなく、軸の取り違えを防ぐ印

AQ0053 §2.2（pp.2–3）, Table 20 と flag 導出では、`nnpfc_purpose` の `0x400` が cross-layer filtering、すなわち入力 picture の layer identifier が異なることを示す。[7]

```text
CrossLayerFlag = ( ( nnpfc_purpose & 0x400 ) > 0 ) ? 1 : 0
```

説明用に一般画質改善の `0x01` と組み合わせて `nnpfc_purpose = 0x401` と置けば、`CrossLayerFlag = 1` になる。これは例の値であって、新しい flag 自体の名前やビット値は上の原文に従う。`nnpfc_purpose = 0x400` 単独も本文で扱われ、用途は application と `nnpfc_application_purpose_tag_uri` による、とされる（§2.2）。[7]

混ぜてはいけないのは、次の二つの防御である。

| 読み手 | 原文が述べる防御 | 読み分け |
|---|---|---|
| 新ビットを扱わない legacy decoder | この新ビットを立てた NNPF を ignore するため、同一レイヤー内の時間方向入力を選ばなくなる、という設計意図（Abstract / §2.1） | 未知ビットだけを取り除いて既知用途の NNPF として実行する、という説明ではない。ここでは各旧版・各実装の動作検証まではしていない。[7] |
| この提案を理解する側 | **non-scalable-nested NNPFA** の関連 NNPFC から `CrossLayerFlag = 1` が得られるとき、その NNPFA を **“should ignore”**（§2.3, D.12.11.1, p.4） | こちらは activation の置かれ方と cross-layer flag の組合せを見る。原文の `should` を `shall` に強めない。[7] |

従って上の抽出後の例では、新側は「残った L0 で2枚を探し直す」のではなく、cross-layer 用なのに non-nested となった **NNPFA を ignore することが推奨される**。一方、この新側の purpose 予約値規則は `2048`–`65535` の NNPFC を `shall ignore` とする。新側が `0x400` 自体を未知の値として捨てる、という話ではない（§2.2 p.3 と D.12.11.1 p.4）。[7]

## 4. nested のままなら、同じ AU で必要な全入力を確認する

D.12.11.1 の v2 本文は、NNPFA が scalable nesting 内にあり、`sn_ols_flag = 0`、`sn_subpic_flag = 0`、関連 NNPFC の `CrossLayerFlag = 1` のときに D.12.11.3 を適用する（AQ0053 p.4）。[7]

その先は、説明用に次の順で読むとよい。ただし以下は読解用手順であり、規格の完全な実装アルゴリズムではない。

1. active な scalable-nested NNPFA の対象 AU を `currAu` とする。[7]
2. **各 `NestingLayerId[i]` に対応し、かつ `PictureOutputFlag = 1` の picture が currAu に全てあるか**を調べる。1つでも満たさなければ、その AU に NNPF は **“not applied”**。全てあれば **“may be applied”** であり、常に推論を実行せよという意味ではない（D.12.11.3 冒頭, p.4）。[7]
3. `currPic` は `NestingLayerId[ 0 ]` の picture。本例なら `A(t)`。NNPFC は `nnpfc_id = nnpfa_target_id` で関連付ける。[7]
4. 入力数・flag・寸法等の適合条件を確認し、`NestingLayerId` の **配列インデックスに対応するスロット**へ画素配列を渡す（pp.4–5）。任意に並べ替えたり、現在 picture と過去 picture の順序へ戻したりしない。[7]

```text
nested のまま AU(t) を調べる場合

ケース             L0           L1                       結果
全入力あり         A(t), out=1  B(t), out=1               適用し得る
入力 picture 欠落  A(t), out=1  なし                      この AU は非適用
出力条件を満たさず A(t), out=1  B(t), out=0               この AU は非適用

非適用のとき B(t−1) や A(t−1) で穴埋めする規則ではない。
```

これは **nested のままの入力成立性検査**であり、前節の **non-nested NNPFA の ignore** と別の判定である。両者を「入力が足りなければ ignore」の一文に潰さない。[7]

### 入力の順序と、picture 欠落／色差欠落の違い

D.12.11.3（p.5）では、`nnpfc_inp_order_idc` が `0, 2, 3` の場合、`NestingLayerId[i]` の luma sample array を `CroppedYPic[i]` に割り当てる。したがって本例の luma はスロット0が `A(t)`、スロット1が `B(t)`。`nnpfc_inp_order_idc` は成分の扱いにも関わるが、ここで示す picture とスロットの対応を勝手に時間順にするものではない。[7]

`nnpfc_inp_order_idc` が `1, 2, 3` の場合は色差配列を対応する `CroppedCbPic[i]` / `CroppedCrPic[i]` に割り当てる。picture は存在するが色差配列を持たない場合、原文は色差 sample を `1 << (inBitDepth[ 0 ] − 1)` で埋める。この規則を、冒頭の **picture 自体が欠ける場合の非適用**を回避する口実にしてはいけない。[7]

## 5. 適合条件を例に当てる

次は option 2 の該当本文に書かれた条件であり、規格全体の適合条件を網羅したチェックリストではない（AQ0053 §2.2 p.3、§2.3 D.12.11.3 pp.4–5）。[7]

| 条件 | 本例での読み方 |
|---|---|
| `CrossLayerFlag = 1` なら `nnpfc_num_input_pics_minus1 > 0` | cross-layer は複数入力。1枚に縮めて逃げない。[7] |
| `nnpfc_num_input_pics_minus1 + 1 = NestingNumLayers` | 本例は2入力・2指定レイヤーで一致。[7] |
| 関連 NNPFC の `PictureRateUpsamplingFlag = 0` かつ `TemporalExtrapolationFlag = 0` | この cross-layer interface を時間方向の補間・外挿と混ぜない。[7] |
| 各入力の `inWidth[i]`, `inHeight[i]`, `inBitDepth[i]` がそれぞれ等しい | 本例は同じ cropped 寸法・同じ picture bit depth と仮定。幅と高さが互いに等しい、という意味ではない。[7] |

`inWidth[i]` は `pps_pic_width_in_luma_samples − SubWidthC * (pps_conf_win_left_offset + pps_conf_win_right_offset)`、`inHeight[i]` は対応する高さから `SubHeightC * (pps_conf_win_top_offset + pps_conf_win_bottom_offset)` を引く。単に coded width/height の比較ではなく、原文で導出した入力寸法の比較である（AQ0053 p.4）。[7]

**原文の留保：** `inBitDepth[i]` の導出文は AQ0053 p.4、AQ2032 p.44 の両方に **“is set equal to 0 the value of BitDepth”** と残る。描画と XML の双方で余分な `0` を確認し、この箇所は削除履歴や直接の打消線で消された文字ではなかった。上の10-bit例は「各 picture の BitDepth を使う」という文脈上の意図に沿う説明用仮定であり、この不整合を黙って校訂した厳密な適合判定ではない。[7][14]

## 6. v2 の変更履歴と AQ2032 本文を突き合わせる

重要なのは、「nested なら CrossLayerFlag は必ず1でなければならない」とだけ覚えないこと。AQ0053 §2.1 の概要にはその趣旨の一文が残る一方、§2.3 の D.12.11.1 では、`sn_ols_flag = 0` / `sn_subpic_flag = 0` の nested NNPFA に対して CrossLayerFlag を1とする **独立の `shall` 文が削除**されている。代わりに、D.12.11.3 を使う条件に **`and CrossLayerFlag ... is equal to 1` が挿入**されている。p.4 の変更表示と XML の `w:del` / `w:ins` の両方で区別した。[7]

従ってこの読解例は、残った概要だけから「全 nested NNPFA に対する独立の適合義務」を復活させず、**v2 の変更後本文にある条件分岐**として読む。これは `CrossLayerFlag = 0` の任意の nested NNPFA の振舞いまで、ここで完全に規定できるという意味でもない。[7]

| 照合事項 | AQ0053-v2 | AQ2032 内部 v3 本文 |
|---|---|---|
| `0x400` と用途範囲 | §2.2, pp.2–3 | option 2, p.42 に対応記述。[14] |
| CrossLayerFlag 導出・複数入力条件 | §2.2, p.3 | p.43 冒頭に対応記述。[14] |
| non-nested cross-layer NNPFA を `should ignore` | §2.3 D.12.11.1, p.4 | p.43 D.12.11.1 に対応記述。[14] |
| 独立 `shall` の削除、flag を含む適用条件 | §2.3 D.12.11.1, p.4 の変更履歴 | p.43 に独立 `shall` はなく、flag を含む条件文がある。[14] |
| 必要 picture / output flag の確認、適合条件 | §2.3 D.12.11.3, p.4 | pp.43–44 に対応記述。[14] |
| NestingLayerId による配列割当て | §2.3 D.12.11.3, p.5 | p.44 に対応記述。[14] |

ここまでから言えるのは、**確認した TuC の option 2 本文に、この提案の該当変更が反映されている**こと。AQ0053 全体の最終採択、option 2 の最終方式化、承認済み VVC/VSEI 規格への取り込み、実 decoder の対応までを断定しない。TuC の収録と正式な標準化状態は別に確認する必要がある。[7][14]

## 読み終わりの確認

次を説明できれば、この寄書の要点をつかめている。

- 「2入力」を `[同時刻・別レイヤー]` と `[同レイヤー・別時刻]` に分けられる。
- extraction が nesting を外すことまで含めて、なぜ時間方向の誤選択へつながるか追える。
- legacy 向けの未知用途の扱い、新側の non-nested activation の `should ignore`、nested の入力欠落による `not applied` を区別できる。
- `NestingLayerId[i]` のスロット対応と、入力数・寸法・時間系 flag の制約を確認できる。
- v2 の削除された `shall` を本文の有効な規定として引用せず、TuC 反映を採択確定と取り違えない。

## Sources

[7] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ0053-v2.zip — JVET-AQ0053
[14] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ2032-v4.zip — JVET-AQ2032
