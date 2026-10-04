# AQ0155 v2を読む：NNPFの「更新」は何を意味するか

[NNPF読書案内](nnpf-reading.md) / [文献案内の入口](README.md)

## この一件で身につける読み方

**モデルの形式が分かることと、更新データの適用操作が分かることは別。** AQ0155 v2は、base NNPFに対する更新について、この二つを別々の提案として扱う。読む対象はモデルの画質・学習性能ではなく、受信側が更新の意味を一意に扱えるかという仕様上の問題である。[10]

確認基準日：2026年10月4日。基準資料はH.274 V4（01/2026）、`JVET-AQ0155-v2.docx`、AQ2032の配布パッケージv4に入っている`JVET-AQ2032-v3.docx`。以下のページ番号はLibreOffice 25.8.5.2で描画したページ／表示フッターに基づくので、Word環境で違う場合は節名・検索語を使う。指定箇所の本文、変更表示、DOCXの挿入・削除XMLを照合した。全TuCの視覚点検や実装適合性検証ではない。[2][10][14]

## まず原文を開く順序

1. **H.274 V4 §8.28.1.2、印刷ページ106**：`nnpfc_base_flag`と`Updates are not cumulative`を探す。
2. **AQ0155 v2 §1 Introduction、§2 Further considerations**：何が曖昧で、v2で何を取り下げたかを読む。
3. **同§3.1 Proposal 1、ページ2**：base/updateの形式を揃える提案。
4. **同§3.2 Proposal 2、ページ2–4**：説明文、構文表、新しいTable X、削除された旧表を分けて読む。
5. **AQ2032、ページ46–47**：`nnpfc_update_type_present_flag`とTable XXXを照合する。統合一覧に寄書番号があるだけで、全提案の採用とは判断しない。[2][10][14]

## 1. 現行仕様：updateは直前のupdateではなくbaseに適用する

H.274 V4では、`nnpfc_base_flag = 1`がbase、`0`がbaseに対するupdateを表す。同じ`nnpfc_id`のupdateは累積せず、各updateをそのbaseに適用する。[2]

> “Updates are not cumulative but rather each update is applied on the base NNPF”[2]

説明用にbaseをB、二つのupdateをU・Vと書くと、考えるべき結果は`apply(B, U)`と`apply(B, V)`である。`apply(apply(B, U), V)`ではない。これは依存関係の説明で、更新演算を加算と規定するものではない。

また、V4では`nnpfc_mode_idc = 0`がSEI内のISO/IEC 15938-17（NNR）ビットストリーム、`1`がURIで指定するデータとその形式の識別を表す。`2`はV4では予約値。AQ0155が言及するmode 2を、そのままV4の既存機能として扱わない。[2][10]

**ここでの確認問：どのbaseに対する更新かは分かったとして、その値を「置換する」のか「足す」のかまで分かるだろうか。**

## 2. 困りごと：形式の一致だけでは操作が決まらない

AQ0155のIntroductionは、TuCでONNX・PyTorchなどの形式の識別を拡張する一方、次の問題があると述べる。[10]

- baseとupdateで`nnpfc_tag_uri`が異なり得る。
- 非NNR形式では、updateのテンソルデータをどのように適用するかが曖昧になる。

### 小さな具体例（説明用。原文の実験ではない）

baseのあるパラメータが`10`で、updateに対応する値`2`があるとする。

- **置換**なら結果は`2`。
- **アプリケーションが加算と別途定めている場合**なら結果は`12`。

どちらも「同じ形式で数値を受け取れた」だけでは区別できない。AQ0155はNNRには更新用の仕組みがあると説明し、非NNRの更新操作の識別を問題にしている。本案内ではNNR仕様自体を独立に精査しておらず、この位置付けは寄書の説明に基づく。[10]

## 3. Proposal 1：baseとupdateの形式を揃える

AQ0155 v2 §3.1は、同じCLVS内で同じ`nnpfc_id`を持つbase/updateについて、次の制約を提案する。[10]

- **両方に`nnpfc_tag_uri`がある場合**：その値を同じにする。
- **それ以外**：mode 0、または存在するtag URIが`tag:iso.org,2023:15938-17`であるという、原文のNNR側の条件を追う。

ここを単に「`nnpfc_mode_idc`を同じにする提案」と言い換えない。形式の識別とデータの搬送方法は別であり、原文はtag URIの有無を場合分けしている。

この提案で防ごうとするのは、例えばbaseをある形式で扱い、updateだけ別の形式として解釈する状況である。しかし、**形式が同じでも置換かアプリケーション定義の操作かは決まらない**。それがProposal 2の役割になる。

**反映状況の限界：** AQ2032の冒頭統合一覧にはAQ0155があるが、取得版のNNPF部分と全文検索では、Proposal 1に対応する同一tag URI制約を確認できなかった。「未確認」であって「否決された」という意味ではない。採否理由や別文言での反映は、議事録等なしに確定しない。[14]

## 4. Proposal 2：更新操作の種類を識別する

AQ0155 v2のTable XとAQ2032のTable XXXは、次の値の意味を示す。[10][14]

- **`nnpfc_update_type_idc = 0`**：updateに存在するパラメータ値が、baseの対応する値を置き換える。
- **`1..13`**：予約。
- **`14..15`**：アプリケーションが定める。

> “The neural network parameter values present in the update (e.g., weights and biases) replace the corresponding values in the base NNPF”[10]

### 誤読しやすい二点

**パラメータ置換は、モデル全体を別物に入れ替えることではない。** Table Xの0は、updateに存在する値とbaseの対応する値についての記述である。全パラメータを必ず送るとも、topologyを任意に置き換えるとも書いていない。§2は、base_flagが0のメッセージによるfull NNPF replacementが現在許されないとのレビュー指摘を説明している。[10]

**14・15は「加算」を規格化した値ではない。** §2ではアプリケーション定義の処理の例としてbaseパラメータへの加算を挙げるが、表の意味はあくまで`Determined by the application`。加算方法を含む外部の取り決めが分からなければ、受信側で処理を確定できない。[10][14]

## 5. 変更履歴を読む：説明文だけでは条件を取り違える

### 原文で見えた変更

AQ0155 v2ページ3では、次の条件の`== 0 && !NnpfcNnrFormatFlag`部分が削除表示になっている。DOCXでも同部分が`w:del`であることを確認した。[10]

```text
変更前側に見える条件：if( nnpfc_base_flag == 0 && !NnpfcNnrFormatFlag )
削除を反映した条件：  if( nnpfc_base_flag ) {
```

その内側に`nnpfc_update_type_present_flag`、さらにそれが真なら`nnpfc_update_type_idc`がある。AQ2032ページ46の構文表でも`if( nnpfc_base_flag )`を確認した。したがって、**確認した構文上はbase側で更新種別の情報を読む形**であり、「各updateメッセージに毎回この値が載る」とは説明できない。ほかの外側の構文条件もあるので、この断片だけを完全なparserとして使わない。[10][14]

AQ0155ページ4には、`NnpfcNnrFormatFlag`の導出と旧Table Xの削除表示がある。ページ3の新Table Xと合成して一つの値表にしない。[10]

### なお原文に残る確認点

- AQ0155 §3.2の導入文は非NNRのupdateで条件付ける説明を残しており、削除後の構文条件とは読み合わせが必要。
- AQ0155とAQ2032の確認した構文表では、`nnpfc_update_type_present_flag`のDescriptor欄が空白。名前だけから`u(1)`と補完しない。`nnpfc_update_type_idc`には`u(4)`が見える。
- 意味記述には`nnpfc_update_type_idc`に加えて`nnpfc_update_type`という表記も残る。後者を黙って前者に修正して引用しない。

これらは**取得版を読む際の不整合・記述不足の確認点**であり、公式な不具合認定ではない。本案内は実装可能な完全仕様への修正案を与えるものではない。[10][14]

## 6. 現行規格・WD・TuC・提案の境界

- **H.274 V4**：base/updateと非累積更新の基準。[2]
- **AQ0155 v2**：形式制約と更新操作の識別という二つの提案。v2内の挿入・削除も読む。[10]
- **AQ2032 TuC**：AQ0155の統合記録があり、update typeの構文・意味・値表を確認できる。ただしProposal 1まで反映済みとは確認できない。[14]
- **AQ2006 V5 WD1／AR0041 v4の全文添付**：NNPF tag URIの拡張を読む資料。AR0041の取得した全文添付では`nnpfc_update_type`を確認できず、TuCのupdate typeをV5 WDに入った機能として扱わない。[13][3]

「AQ0155はTuCへ統合された」という短い説明から、「二つの提案が全て規格になった」へ飛躍しない。

## 7. 杭州AR寄書への対応付け

2026年10月4日の公開registerを、検索条件なしのページとCSVでも確認した。取得できた登録行はAR0041〜AR0044で、本文確認済みのNNPF関連の橋渡し資料はAR0041である。公開一覧に見つからないことは、寄書が存在しないことの証明ではない。[4]

**AR0041 → V5 WD1の全文中のtag URI → AQ2006 → AQ0155 Introductionの形式拡張という背景**、という関係で読む。AR0041を「AQ0155 Proposal 2の採用確認資料」にはしない。AR0042／AR0043は公開タイトルではGSC系、AR0044はAVC/HEVC/VVC errataであり、タイトルだけでNNPF更新操作の必読資料には追加しない。これらの本文精読はしていない。[3][4]

新しいAR寄書を読むときは、次だけを埋めればよい。

- どの版・草案の、どのsyntax elementを変えるか。
- AQ0155の形式制約／更新種別／base側の信号のどれに関係するか。
- 寄書の説明、変更履歴を反映した構文、TuCの本文が一致するか。
- 新しい提案なのか、既存案の修正なのか、統合済み本文の説明なのか。

この確認は一回の公開状況点検であり、自動監視や将来の再確認を設定したものではない。

## 読み終わりの確認

次のように説明できれば、この一件は一区切りになる。

> V4ではupdateはbaseに対して非累積に適用する。AQ0155は、baseとupdateの形式を揃えることと、非NNRで更新操作を識別することを別々に提案する。v2の値表では0が対応パラメータの置換、14・15がアプリケーション定義であり、モデル全体の置換や一般的な差分加算の規格化ではない。取得したTuCでは更新種別の記述を確認したが、Proposal 1の反映は未確認。更新種別の構文はbase側の条件で、説明文やDescriptor欄には確認点が残る。

次にAQ0052／AQ0058へ進む場合は、この型のうち「旧decoderが構文をどう読むか」を中心に置く。全ての資料をもう一度通読する必要はない。

## 確認範囲

- H.274 V4の指定節を本文で確認。AQ0155の技術本文、TuCの対応する構文・意味を対照。
- LibreOffice描画のAQ0155ページ2–4、TuCページ46–47を画像で確認し、重要な削除条件をDOCX XMLでも照合。Wordと同一の改ページ・表示を保証しない。変換時に書式関連の警告があったため、描画だけを根拠にしていない。
- Proposal 1の未確認は、TuCのNNPF部分の読取りと全文の関連語検索に基づく。議事録本文による採否理由の確認はしていない。
- 数値例は編集上の説明。ニューラルネットワークの実行、bitstreamの生成・parser検証、性能再現はしていない。
- [確認記録](nnpf-aq0155-evidence.json)は対象版・位置・観察を記録する。第三者の全文、描画PDF・画像、個人の読了記録は公開しない。

Sources:
[2] https://www.itu.int/rec/T-REC-H.274-202601-I/en — H.274 V4 (01/2026)
[3] https://jvet-experts.org/doc_end_user/current_document.php?id=17234 — JVET-AR0041
[4] https://jvet-experts.org/doc_end_user/current_meeting.php?id_meeting=208&search_id_group=1&search_sub_group=1 — Hangzhou register
[10] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ0155-v2.zip — JVET-AQ0155
[13] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ2006-v4.zip — JVET-AQ2006
[14] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ2032-v4.zip — JVET-AQ2032
