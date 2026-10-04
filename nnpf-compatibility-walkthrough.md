# AQ0052／AQ0058を読む：旧decoderはどこで読み違えるか

[NNPF読書案内](nnpf-reading.md) / [AQ0155の更新操作](nnpf-aq0155-walkthrough.md)

## 結論と確認範囲

**既存の条件の内側へ新しい構文を挿入するだけでは、旧decoderはそれを新機能だと識別できない。** この一件では、新しい情報を後方へ移し、旧decoderに「このNNPFC SEIメッセージを無視すべき」と分かる値で条件付けする設計を読む。「拡張を無視する」と「新機能も使える」は別である。[2][6][9]

確認基準日：2026年10月4日。対象はH.274 V4（01/2026）、AQ0052 v1、AQ0058 v2、AQ2032配布v4内の`JVET-AQ2032-v3.docx`。寄書とTuCの指定本文を対照し、LibreOffice描画のAQ0052ページ1–2、AQ0058ページ4–6、TuCページ20・25を画像確認した。範囲表記はDOCXのrun単位の取り消し線でも照合した。ページはこの描画環境の番号であり、検索語・節名を併用する。[6][9][14]

**重要な留保：** 統合案・TuCで拡張の構文を確認できたが、同じ本文にはその利用値と予約範囲の不整合が残る。以下は設計意図と構文の局所例であり、完成した仕様の適合性証明ではない。

## 1. 現行V4の、何を基準にするか

H.274 V4 §8.28.1.1の構文では、時間外挿が有効な場合に`nnpfc_extrapolated_pics_minus1`を読む。その後は空間外挿の条件付き要素、`nnpfc_component_last_flag`、`nnpfc_inp_format_idc`、`nnpfc_auxiliary_inp_idc`などが続く。V4にはこの位置の`nnpfc_num_alt_instances_minus1`や`nnpfc_mult_inferences_flag`はない。[2]

旧decoder側の識別規則は§8.28.1.2で確認する。

- `nnpfc_out_order_idc`の4〜255：そのNNPFC SEIメッセージを無視する。
- `nnpfc_auxiliary_inp_idc`の8〜255：そのNNPFC SEIメッセージを無視する。[2]

この規則の利用が提案の鍵になる。単に「知らないビットを飛ばす」のではなく、**メッセージ単位で適用対象から外す**という意味で読む。実際のdecoderが内部でどの順番で検査・スキップするかは、ここでは実行確認していない。

## 2. 問題になる入力例：最初の読み違いを追う

AQ0052 §1 Problem Statement、AQ0058のProposalは、以前のTuCでは追加情報が既存の`TemporalExtrapolationFlag`だけで条件付けされている、と問題提起する。この履歴上の構文は両寄書の比較対象として確認したもので、以前のAP2032全編を独立検証したものではない。[6][9]

### 条件を絞った模式例

時間外挿は有効、空間外挿やtone mappingなどの介在する条件付き要素はないと仮定する。図は`nnpfc_extrapolated_pics_minus1`を読み終えた直後から始める。完全なSEI payloadではなく、値の全制約を満たす試験bitstreamでもない。

```text
変更前V4が期待するもの
  → component_last_flag → inp_format_idc → auxiliary_inp_idc → …

問題提起された追加位置
  → num_alt_instances_minus1 → mult_inferences_flag → component_last_flag → …
       ↑ 旧decoderには、この要素が増えたことが分からない
```

説明用に`num_alt_instances_minus1 = 1`、`mult_inferences_flag = 1`、本来の`component_last_flag = 1`を置く。寄書のDescriptorは順に`ue(v)`、`u(1)`で、V4のcomponent flagも`u(1)`である。[2][6]

```text
送られた局所的なビット列： 010 | 1 | 1
追加構文を知る読み方：     count | flag | component=1
V4の最初の読み方：         0 | 残り1011…
                          └ component=0 と読む
```

最初の1ビットですでに意味が変わる。その後のparserの全挙動やクラッシュは、この部分例から主張しない。値をいくつか試す以前に、**旧版が知っている条件だけでは構文の増加を識別できない**ことが問題である。

この局所例は[実行用スクリプト](scripts/nnpf_compat_example.py)で確認できる。

```sh
python3 scripts/nnpf_compat_example.py
```

出力は`bits: "01011"`、拡張を知る側のcomponent値は1、V4の最初の読み取り値は0。実decoderのログではなく、この説明のための短いモデルの出力である。

## 3. 当初案と統合案：何を残し、何を変えたか

### AQ0052 v1：出力順序の値を使う案

§2 Overview／§3 Proposed specification text changes、ページ1–2を読む。

- 時間外挿の元の位置から追加要素を取り除く。
- `nnpfc_out_order_idc & 4`で追加要素を条件付ける。
- 低位部分の出力順序を`outOrderIdc = nnpfc_out_order_idc & 3`で扱う。
- 複数候補があることを条件のビットで示すため、個数を`minus1`から`minus2`へ変更する。[6]

V4はout_orderの4以上を認識対象にせずメッセージを無視する、という規則を利用する。この案を後述のauxiliaryビットの案と混ぜない。

### AQ0058 v2：Option 1の統合案

読む中心はページ4からの **“Modification of Option 1 based on a merge with JVET-AQ0052.”**。前方の元Option 1や、後方のOption 2と区別する。[9]

- 追加要素を`nnpfc_auxiliary_inp_idc`の後へ移す。
- 条件には`nnpfc_auxiliary_inp_idc & 0x10`を使う。AQ0052のout_order側のビットではない。
- 統合部分では`nnpfc_num_alt_instances_minus2`を使い、その条件内で`nnpfc_mult_inferences_flag`を読む。元Option 1にあった「minus1が0より大きければflagを読む」という条件は削除表示になっている。
- 複数text promptにも同じ拡張ビットの条件を加える。ただしtext promptのビット、inband flag等の外側の条件も必要で、0x10だけでpromptが必ず存在するわけではない。[9]

**統合の要点：** auxiliary側へ移す設計と、複数候補をビットで識別して`minus2`を用いる設計が組み合わされている。二つの寄書を最後まで独立した競合案として読まない。

Option 2はmetadata sectionへ移す別案として残る。元Option 1・統合部分・Option 2の構文をつなぎ合わせて一つの仕様にしない。[9]

## 4. 提案後の分岐：旧側は無視、新側は追加構文へ

以下は**統合案の構文が意図する流れ**。次節の予約範囲の不整合があるため、適合bitstreamの実演とは呼ばない。

```text
共通部分を読む
  → auxiliary_inp_idc（例：16）
       ├─ V4の規則：8〜255なので、このNNPFC SEIメッセージを無視
       └─ 拡張の構文を追う場合：0x10が立っている
             → num_alt_instances_minus2
             → mult_inferences_flag
             → ほかの条件が成立するときだけ複数prompt
```

例のauxiliary値16の`ue(v)`表現は`000010001`。`minus2 = 0`なら候補数は2。この計算も上記スクリプトに含めている。

守りたい性質は、**新しい長さ・意味の情報を、旧構文の別の要素として誤解釈させないこと**である。旧decoderが複数推論を実行できること、NNPF出力が新decoderと一致すること、全製品で実装が正しいことを保証するものではない。

## 5. TuCで確認できる部分と、完成仕様とは扱えない理由

AQ2032の冒頭統合一覧にAQ0058がある。ページ20の構文表では次の並びを確認した。[14]

```text
nnpfc_auxiliary_inp_idc                         ue(v)
if( ( nnpfc_auxiliary_inp_idc & 0x10 ) > 0 ) {
    nnpfc_num_alt_instances_minus2              ue(v)
    nnpfc_mult_inferences_flag                 u(1)
}
```

同じ表では複数promptの条件も確認できる。したがって、「AQ0058の統合部分と対応する局所構文がTuCにある」とはいえる。**全提案の採否・編集意図・承認規格への採用までを証明するものではない。**

### 予約範囲の不整合をそのまま残す

AQ0058の統合部分ページ6とTuCページ25では、auxiliary値の予約範囲の開始が、取り消された`8`から`16`へ変わっている。一方で、同じ本文は`& 0x10`が16になる場合の追加情報を定義している。[9][14]

つまり、取得本文のままでは、**拡張を示す値が16以上になるのに、16以上を予約・無視対象としている**。単純抽出に出る`816`は一つの数値ではなく、取り消し線付きの8と残る16の連結である。画像とXMLの`w:strike`を確認したので、OCR誤読だけの問題ではない。

この案内では16を別の値に修正しない。正しい予約範囲を推定して「これで互換性問題は解決済み」ともしない。**旧V4が無視する仕組みは説明できるが、新仕様側も矛盾なく使えることは未確認**という境界を保つ。

TuCは複数の編集指示・断片を含む。ここで確認した断片を完全なNNPFC parserに仕立てて、規格の正しさを検証したことにはしない。

## 6. 未解決点は、解消に必要な資料と組にする

- **この読解例の予約範囲**：後続の訂正版、会合報告・編集指示、統合済みの一貫した仕様本文で確認する。採否理由は未確認。
- **AQ0155 Proposal 1の形式制約**：同一tag URIの制約が入った本文、または扱いを明記した議事録が必要。TuC内で見つからないだけで却下とはしない。
- **AQ0155の構文条件・Descriptor欄・名称表記**：対応する修正文または編集上の説明で確認する。非NNRの場合でも更新種別が必ず指定されるとは扱わない。

これは確認待ちの論点一覧であり、外部への問い合わせ送信や自動監視を設定したものではない。

## 読み終わりの確認

次を原文の位置付きで説明できれば一区切り。

1. 時間外挿が既存機能であるため、追加情報の識別条件としてそれだけでは足りない理由。
2. V4が最初にどの情報を誤読するか。ただし例の介在要素を除いた仮定を添える。
3. AQ0052のout_order案と、AQ0058統合部分のauxiliary案の違い。
4. 「旧側がメッセージを無視する」ことと「新仕様として矛盾なく利用できる」ことの違い。

## 確認の限界

指定本文・指定ページの変更表示・予約範囲のXMLを確認した。LibreOfficeの描画には書式関連の警告があるため、重要箇所は画像だけに依存していない。完全な実decoder、実SEI payload、映像、NNモデルは実行していない。スクリプトの成功は模式例の整合確認であり、JVET/VSEI適合性試験ではない。原文・描画物・抽出全文は公開リポジトリに含めない。

Sources:
[2] https://www.itu.int/rec/T-REC-H.274-202601-I/en — H.274 V4 (01/2026)
[6] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ0052-v1.zip — JVET-AQ0052
[9] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ0058-v2.zip — JVET-AQ0058
[14] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ2032-v4.zip — JVET-AQ2032
