# 杭州JVET会合に向けたNNPF読書案内

[文献案内の入口](README.md) / [目的別の読み順](reading-queue.md)

## 目標と対象

対象は第44回JVET会合、杭州、2026年10月17〜23日、文書記号AR。目標はNNの一般知識を増やすことではなく、NNPF寄書の問題設定・変更対象・互換性・提案の状態を説明できること。[1]

確認基準日：2026年10月4日。会合文書の追加・改訂や採否は、この時点の確認範囲に限定する。

この案内で基準にする現行規格はITU-T H.274 V4（01/2026）。V3（09/2023）は旧版なので、2024年の概説を読む場合も現在の節番号・機能と区別する。V4の公式PDFと以下のJVET文書の指定本文を確認した。全編精読・実装検証はしていない。変更表示の画像確認は、[AQ0155の読解例](nnpf-aq0155-walkthrough.md)に記したAQ0155とTuCの指定箇所に限定する。[2]

**最小の進め方：V4のNNPF → AQ2006とAR0041 → AQ0155 → AQ0052とAQ0058 → AQ0053。TuCは対応箇所を引く。** これは学習上の推奨順であり、全資料の通読要求ではない。

## 最優先：現行仕様と、次の仕様の境界

### 1. ITU-T H.274 V4（01/2026）

- 役割：採用済みの動作を調べる基準。
- 読む場所：§8.28.1.2（NNPFC semantics）、§8.28.2.2（NNPFA semantics）。構文を変更する寄書に出会ったら、それぞれ§8.28.1.1、§8.28.2.1へ戻る。
- 最初に探す語：`nnpfc_id`、`nnpfc_base_flag`、`nnpfc_mode_idc`、`nnpfc_tag_uri`、`nnpfc_uri`、`nnpfc_purpose`、`nnpfa_target_id`、`nnpfa_target_base_flag`。
- 読む問い：NNの特性・所在・更新を示すことと、特定画像でそのNNの使用を有効化することはどう違うか。
- 終了条件：base/updateとcharacteristics/activationを区別し、対象寄書が触るsyntax elementを規格で探せる。
- 後回し：他のSEI全種類、NNPFの全テンソル整形式。入力配置を変える寄書の場合だけ、その箇所を精読する。
- 注意：V3とV4で節番号が異なるため、旧版の節番号をそのまま使わない。[2]

### 2. JVET-AQ2006 — Additional SEI messages for VSEI version 5 (Draft 1)

- 確認ファイル：`JVET-AQ2006-v4.docx`。
- 役割：前回会合からV5作業草案へ何が統合されたか、変更指示を確認する。
- 読む場所：冒頭の統合リストのNNPF項目と、`In subclause 8.28.1.2, replace the semantics of nnpfc_tag_uri`から始まる変更本文。
- 読む問い：frameworkとversionを識別するtag URIをどう表現するのか。それはNNデータの所在を示すURIとどう違うか。
- 終了条件：V4での記述とWDの変更箇所を一組対応させられる。
- 後回し：film grain、display overlaysなどNNPFと無関係な追加SEI。
- 状態：作業草案であって承認済みV5規格ではない。[13]

### 3. JVET-AR0041 — Full VSEI text with change marks for changes in VSEI v5 WD1

- 確認パッケージ：`JVET-AR0041-v4.zip`。表紙の寄書と`JVET-AR0041-v4_spexText.docx`の全文添付を区別する。
- 役割：AQ2006の変更を全文の文脈で読むための伴走資料。別の新方式の原著として読むものではない。
- 読む場所：表紙のAbstract、添付のNNPFC節、特にtag URI関連。
- 読む問い：AQ2006の変更指示が、現行のどの段落に入るのか。
- 終了条件：現行V4／V5 WD／当該寄書の追加提案を別々に示せる。
- 注意：表紙はAQ2006に記録されない軽微な編集改善等も含むと説明している。AQ2006と完全同一の変更集合とは扱わない。変更履歴を無視した抽出テキストだけで、削除・追加の最終的な効果を判断しない。[3]

## 次に読む：実際の寄書で論点をつかむ

### 4. JVET-AQ0155 v2 — On NNPFC updates

**最初の具体的な練習に推奨。**

[原文対照付きの読解例](nnpf-aq0155-walkthrough.md)では、V4の非累積更新、パラメータ置換の具体例、変更履歴を反映したbase側の構文条件を追う。Proposal 1のTuC反映は未確認として、Proposal 2の確認済み本文と分けている。

- 読む場所：Abstract → Introduction → Further considerations → Proposals 1/2 → 対応する構文・意味。
- 問題：NNR以外にONNX/PyTorch等の形式を用いる場合、base NNへのupdateが具体的に何を意味するか。
- 比較するもの：baseとupdateの形式の整合、パラメータの置換、アプリケーション定義の処理。
- 重要な版差：v2ではレビュー後にproposal 2が修正されている。v1の提案を最終形と取り違えない。
- 終了条件：「同じupdateという名前でも、適用操作が曖昧だと受信側で何が決まらないか」を説明できる。
- 状態の確認先：AQ2032のNNPF統合リストと対応本文。update typeの構文・意味は確認できるが、Proposal 1の同一tag URI制約の反映は未確認。TuCへの統合を承認規格への採用と呼ばない。[10][14]

### 5. JVET-AQ0052 v1 ＋ JVET-AQ0058 v2 — 複数推論と後方互換性

- 読む場所：AQ0052のProblem Statement/Overview、次にAQ0058 v2のAbstract/Introduction/Proposalと変更構文。
- 問題：既存の条件分岐の内側に新しいsyntax elementを挿入すると、旧版decoderが後続ビットを別の要素として誤解釈する可能性がある。
- 読む問い：新しい機能を表す値・flagと、その後の構文を読む条件を、旧版decoderがどう扱うか。
- 版の注意：AQ0058 v2はAQ0052とのmerged proposalの記載がある。AQ0052の当初案とAQ0058 v2を、最後まで別々の競合案と決めつけない。
- 終了条件：変更前後の構文条件を一箇所ずつ追い、旧decoderが安全に無視できるのか、誤って読み続けるのかを説明できる。
- 状態の確認先：AQ2032のAQ0058統合記録と対応本文。[6][9][14]

### 6. JVET-AQ0053 v2 — On multilayer NNPF

- 読む場所：Abstract、Use cases、Background、sub-bitstream extractionの問題説明、提案したpurposeのbit。
- 問題：複数の入力画像が「時間の違う画像」なのか「別layerの画像」なのか。scalable nestingから取り出した後にもその意味を保持できるか。
- 先に必要な概念：layer、CLVS、出力順、scalable nesting。分からない語だけV4と関連するコーデック側の仕様へ戻る。
- 終了条件：layerを抜き出す操作が、NNの入力選択にどんな誤解を生むか説明できる。
- 状態の確認先：AQ2032のAQ0053統合記録と対応本文。v2にはJVETレビューに従う修正の記載がある。[7][14]

## 通読せずに使う索引・状態確認資料

### JVET-AQ2032 — Technologies under consideration for future extensions of VSEI (version 13)

- 役割：まだ検討中の拡張の参照先。
- 読む場所：冒頭の統合記録とNNPF部分のみ。AQ0053、AQ0058、AQ0059、AQ0155がNNPF統合リストに並ぶ。
- 重要：V5 WDへ移ったNNPF tag URI拡張も、他のNNPF拡張との関係でTuCに繰り返し残されている旨の注記がある。「TuCに載っているから全て未移行」とも判断しない。
- 版の注意：取得した配布リンクは`JVET-AQ2032-v4.zip`だが、中の主要Wordファイル名は`JVET-AQ2032-v3.docx`。リンク版と内包ファイル名をそのまま記録する。
- 原文の全文と変更履歴はWordで確認する。抽出した表の順序だけで構文の正否を確定しない。[14]

### JVET-AQ0054 v2 — NNPF extension for VSEI version 5

- 役割：何をTuCからWDへ移そうと提案したか、成熟度・ソフトウェア・利用例の見方を知る。
- 読む場所：Abstractとsummary tableのNNPF部分。
- 最重要の対比：本寄書の移行提案にはauxiliary input、tag URI、in-band modeが挙げられるが、AQ2006のNNPF移行記録・変更本文で確認する対象はtag URI。提案リストを採択リストに置き換えない。
- 全機能の採否理由をこの二資料だけで断定しない。[8][13]

### JVET-AQ0009 — AHG report: SEI message studies (AHG9)

- 役割：関連寄書を拾う索引。
- 読む場所：NNPF関連の寄書一覧。
- 注意：第42回から第43回までの活動を報告する入力資料。第43回の最終採否や、その後の活動の報告として使わない。次回のAHG9報告が公開されたら索引の基準を置き換える。[5]

## 対象寄書が出たときだけ追加する

- **AQ0157 v1 — On NNPFC framework formats and model parameter compression**：モデルのtopologyと圧縮パラメータを分離して扱う提案。ONNX/PyTorchとNNRの関係が議題なら読む。提案本文を確認したが、最終採否は確定していない。[11]
- **AQ0196 v1 — Loss concealment purpose for NNPFC SEI message**：受信側で検出する欠落に対し、通常のNNPFC/NNPFAの組合せだけで足りるかを問う。損失隠蔽が議題なら読む。提案本文を確認したが、最終採否は確定していない。[12]
- **Standards-Based Neural-Network Post-Filters for Improved Video Quality（MHV 2024）**：NNPFC/NNPFAという全体像がまだ難しい場合の概説候補。出版社要旨・書誌の確認にとどまる。V3時点の説明なので、現在の規格・WD・TuCの代わりにはしない。[16]

一般的なCNN/VAE教科書、DVC/DCVCの全編、NNVCの全in-loop filter資料は、この目的の共通前提にはしない。特定寄書がモデル構造・学習方法・実験性能を論点にしている場合に、その原論文と実験条件を追加する。

## 寄書を読めたかの確認メモ

各寄書を次の五行で説明できれば、会合の議論へ入る足場になる。

1. **現行動作**：どの版・節・syntax elementを基準にしているか。
2. **困りごと**：どんな入力、操作、旧decoderで問題が起きるか。
3. **変更案**：何を追加・制約・削除するか。
4. **互換性と負担**：旧実装の挙動、モデル/信号の追加情報、実装上の影響は何か。
5. **状態と未解決**：現行規格、WD、TuC、個別提案のどこにあり、何がまだ分からないか。

最初の一件はAQ0155 v2とし、V4のbase/update定義、TuCの対応本文へ往復することを勧める。推奨順は編集判断であり、学習時間・理解度は未測定。

## 確認範囲と不足

- 第44回の公開registerでAR0041を確認した。次回の全NNPF寄書が揃ったとは扱わず、現段階では前回寄書と現在の草案で準備する。[4]
- 第43回のMeeting Report（AQ1000）は登録を確認できたが、確認した詳細ページには配布ファイルがなく、本文を取得できなかった。そのため議事録を読んだとはせず、状態判断は取得したAQ2006/AQ2032の統合記録・本文に限定する。[15]
- ZIP内のWord本文を選択抽出。AQ0155のページ2–4とTuCのページ46–47はLibreOffice描画で変更表示・構文表を画像確認し、重要な削除をXMLでも照合した。他の変更履歴付き資料の視覚点検は未実施。抽出本文を確定済み全文として扱わない。詳細は[確認記録](nnpf-aq0155-evidence.json)。
- 元のPDF/Wordや抽出全文は公開リポジトリへ転載していない。公開資料に基づく読書案内であり、個人の読了記録は含まない。

Sources:
[1] https://jvet-experts.org/doc_end_user/all_meeting.php — JVET meeting archive
[2] https://www.itu.int/rec/T-REC-H.274-202601-I/en — H.274 V4 (01/2026)
[3] https://jvet-experts.org/doc_end_user/current_document.php?id=17234 — JVET-AR0041
[4] https://jvet-experts.org/doc_end_user/current_meeting.php?id_meeting=208&search_id_group=1&search_sub_group=1 — Hangzhou register
[5] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ0009-v1.zip — JVET-AQ0009
[6] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ0052-v1.zip — JVET-AQ0052
[7] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ0053-v2.zip — JVET-AQ0053
[8] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ0054-v2.zip — JVET-AQ0054
[9] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ0058-v2.zip — JVET-AQ0058
[10] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ0155-v2.zip — JVET-AQ0155
[11] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ0157-v1.zip — JVET-AQ0157
[12] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ0196-v1.zip — JVET-AQ0196
[13] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ2006-v4.zip — JVET-AQ2006
[14] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ2032-v4.zip — JVET-AQ2032
[15] https://jvet-experts.org/doc_end_user/current_document.php?id=17219 — JVET-AQ1000 registry, no file obtained
[16] https://dl.acm.org/doi/10.1145/3638036.3640809 — Standards-Based Neural-Network Post-Filters for Improved Video Quality
