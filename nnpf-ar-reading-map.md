# AR寄書からNNPFの背景資料へ戻る案内

[NNPF読書案内](nnpf-reading.md) / [目的別の読み順](reading-queue.md)

## 今、何から読むか

**最初はAR0041 v4の表紙Abstract → 全文添付のNNPFC意味規定 → AQ2006のtag URI変更指示。** 更新操作・複数推論・多層入力の読解例は、AR0041へ一括で採用された機能としてではなく、必要な論点へ戻るための背景資料として使う。[17][13]

確認基準日：2026年10月4日。公開registerを通常URLと検索条件を空にしたURLで取得し、どちらもAR0041〜AR0044の4件だった。ページ送りリンクは確認できなかった。これは取得した公開画面の範囲であり、会合の全提出予定文書、非公開資料、今後追加される寄書を網羅する主張ではない。[4]

## 公開registerの振り分け

タイトルによる一次振り分けである。AR0042〜AR0044は本文未確認なので、NNPFへの間接的関係まで否定しない。[4]

| 寄書 | 公開タイトルの論点 | この学習での扱い |
|---|---|---|
| AR0041 v4 | VSEI v5 WD1の変更表示付き全文 | NNPFに直接戻れる入口。表紙・指定本文・一部変更表示を確認 |
| AR0042 v1 | GSC / HGSI SEIのソフトウェア・CTC結果 | NNPF経路からはいったん外す。本文未確認 |
| AR0043 v1 | GSC VSEI frameworkのexplicit packing mode実装 | NNPF経路からはいったん外す。本文未確認 |
| AR0044 v1 | AVC・HEVC・VVCのerrata | NNPF関連の修正が議題になった場合に本文を確認 |

現時点の公開タイトルからは、AR0041とは別のNNPF個別提案を確認できない。したがって、存在が確認できていないAR寄書とAQ寄書の対応は作らない。[4]

## AR0041を読むための対応

### 基準と変更箇所

- **承認規格の基準**：H.274 V4（01/2026）§8.28.1.2の`nnpfc_tag_uri`と`nnpfc_uri`。[2]
- **変更指示**：AQ2006 v4の`In subclause 8.28.1.2, replace the semantics of nnpfc_tag_uri`から始まる部分。[13]
- **全文内で読む位置**：AR0041-v4.zip内`JVET-AR0041-v4_spexText.docx`のNNPFC意味規定、`nnpfc_tag_uri`、Table 22 “frameworkName values for nnpfc_tag_uri”。LibreOffice描画PDFの118ページ（印刷ページ109）。表紙`JVET-AR0041-v4.docx`とは別ファイル。[17]
- **具体例**：原文の`tag:iso.org,2026:vsei:onnx:13`で、frameworkとversionが何を識別するかを読む。一方`nnpfc_uri`はNNデータを識別するURI。タグをデータの所在と取り違えない。[17]

AR0041のこの箇所は、V4本文にframework/version識別を追加する読み方になる。本文の追加表示を画像とDOCXの`w:ins`で確認した。これはタグの解釈であり、モデルの更新操作や多層画像選択を一括して規定する変更ではない。[17]

### 論点別の戻り先

| 読んでいて生じた問い | 戻る資料 | そこで確認すること | AR0041との関係 |
|---|---|---|---|
| モデル形式と所在をどう識別するか | V4 → AQ2006 → AR0041 | tag URI / URI / framework / version | 今回確認したWD変更本文の直接対象 |
| baseに対する更新とは何か | [AQ0155読解例](nnpf-aq0155-walkthrough.md) | 更新対象、更新種別、TuCとの差 | 背景。更新種別提案のWD採用を意味しない |
| 新構文を旧decoderが誤読しないか | [AQ0052／AQ0058読解例](nnpf-compatibility-walkthrough.md) | 新構文の位置とignore規則 | 背景。TuCの複数推論構文とWDを混ぜない |
| 複数入力は時系列か、別layerか | [AQ0053読解例](nnpf-multilayer-walkthrough.md) | nesting、入力画像対応、抽出後の誤選択 | 背景。CrossLayerFlag提案と承認規格を混ぜない |

取得したAR0041全文の抽出テキストでは`CrossLayerFlag`、`nnpfc_update_type`、`num_alt_instances`を確認できなかった。これは指定識別子の検索結果であり、全変更の意味的な不在証明ではない。auxiliary入力の意味規定は描画PDF122ページ（印刷113）でも確認し、予約範囲は8〜255のままだった。[17]

**読む順の判断**：AR0041のtag URIだけを理解するなら、上の三つの読解例を全て先に読む必要はない。多層入力にまだ触れていない場合は、AQ0053を次の背景学習にする。将来のAR個別提案が公開されたら、その問題設定に合わせて順を入れ替える。

## 互換性の未解決点をどこまで追ったか

AQ0058の詳細ページでは配布版v2まで、AQ2032では配布版v4までを確認した。前回確認した版より新しい公開配布リンクは見つからなかった。AQ1000の詳細ページには今回もダウンロードリンクを確認できず、議事録本文から解決・採否を確定できない。[18][19][15]

AQ2032詳細ページの版一覧には、版番号を表示しない“rejected by the Chair”の行と、v2・v3・v4の配布行が併存する。この表示をAQ0058の提案全体の却下や、配布v4全体の却下と読み替えない。[19]

- **残る問い**：統合案の`auxiliary_inp_idc & 0x10`と、16以上を予約・無視対象にする意味規定は、どの修正本文で整合するか。[9][14]
- **今回の判断**：AR0041は同じ複数推論拡張を規定する修正版として確認できていない。WD側の予約範囲を見て、TuCの不整合が解消したとは言えない。[17]
- **再確認の条件**：AQ0058/AQ2032の改訂、対応するAR個別提案、または議事録・修正指示が入手できたとき。
- **今はしないこと**：推測で予約範囲を書き換えること、同じ版の再読だけを繰り返すこと、未解決を理由に他の学習を止めること。

## 終了条件と確認範囲

AR0041について「基準版」「指定段落」「tagとURIの違い」「背景のTuC提案とは別であること」を説明できれば、この入口は一区切り。資料整備の完了は、読者の理解度を測定したことにはならない。

今回の確認は公開register、AR0041表紙・指定本文、描画PDF118・122ページの目視、tag追加のXML照合、指定識別子検索、改訂リンクと議事録配布有無。AR0041全編の変更履歴監査、他のAR寄書の本文精読、実decoder試験、会合での採否確認はしていない。原本・抽出全文・描画画像は公開リポジトリへ転載しない。

Sources:
[2] https://www.itu.int/rec/T-REC-H.274-202601-I/en — H.274 V4 (01/2026)
[4] https://jvet-experts.org/doc_end_user/current_meeting.php?id_meeting=208&search_id_group=1&search_sub_group=1 — Hangzhou register
[9] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ0058-v2.zip — JVET-AQ0058
[13] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ2006-v4.zip — JVET-AQ2006
[14] https://jvet-experts.org/doc_end_user/documents/43_Geneva/wg11/JVET-AQ2032-v4.zip — JVET-AQ2032
[15] https://jvet-experts.org/doc_end_user/current_document.php?id=17219 — JVET-AQ1000 registry, no file obtained
[17] https://jvet-experts.org/doc_end_user/documents/44_Hangzhou/wg11/JVET-AR0041-v4.zip
[18] https://jvet-experts.org/doc_end_user/current_document.php?id=17017
[19] https://jvet-experts.org/doc_end_user/current_document.php?id=17230
