# 独立候補との比較

既存名簿を渡さない探索から8候補を得た後、親側で既存集合と照合した。これは統計的な独立性や分野代表性の証明ではない。HEVC寄りの探索であり、学習型・誤り耐性・エネルギー/HDR等の空白は残る。

**変更した判断**：基本原理のP06と比較法のP13は維持。一方、速度経路をニューラル方式だけで構成せず、遅延の構成要素と実装設定を追加参照にする。知覚品質経路には理論だけでなく視聴評価の実証研究を接続する。

主候補20件は結果として変わらないが、資料負担が不変という意味ではない。独立候補8件には既存論文2件が含まれ、別教材・規格・書籍・実装文書・論文も含む。追加した参照を全員向け必読にはしない。F01/F02とも別の探索記録である。

## IC01：Block-Based Hybrid Video Coding

- 出典：[書誌/公開資料](https://bpb-us-e1.wpmucdn.com/wp.nyu.edu/dist/b/10258/files/2023/04/Videocoding.pdf)。Yao Wang, Image and Video Processing / ECE-GY 6123, New York University, 2023, 講義資料
- 判定：**教材の代替**。P01/P02の説明で止まる場合だけ閉ループ予測の補助教材にする。全員の前提には増やさない。
- 読む目的：論文の前に、予測→残差→量子化→再構成→参照という基本構造の概念地図を作る。
- 確認範囲：予測、双方向予測、閉ループ構成、符号化器/復号器の一致、残差の変換符号化の入口、末尾のLagrange係数・deadzone量子化説明をテキスト確認。中間省略があり全文精読ではない。図は視覚確認していない。
- 限界：査読論文ではなく教材。教材の数値例や簡略化を一般性能保証として採用しない。

## IC02：Rate-Distortion Optimization for Video Compression

- 出典：[書誌/公開資料](https://cris.fau.de/publications/109995644/?lang=en_GB)。Gary J. Sullivan and Thomas Wiegand, IEEE Signal Processing Magazine, 15(6), 74–90, 1998
- 判定：**維持**。既存P06と同一論文。意思決定原理の入口として維持し、重複登録しない。
- 読む目的：符号化ツールの列挙を、符号量・歪み・探索計算量を伴う意思決定問題として読み替える。
- 確認範囲：FAU書誌、Stanfordコピーの冒頭、制約付き最適化からLagrangianへの説明、近似と意思決定の依存、Bit-Rate Control、Motion Estimationの本文を選択確認。抽出式には欠落・乱れがあり式の完全性は未検証。
- 限界：古い規格の例に基づく。Stanfordの公開授業コピーであり、著者版との同一性・再配布許諾は別途確認が必要。現代実装への数値の直接移植はしない。

## IC03：High efficiency video coding

- 出典：[書誌/公開資料](https://www.itu.int/rec/T-REC-H.265-202601-I)。ITU-T Recommendation H.265 (01/2026), approved 2026-01-13
- 判定：**規範参照**。HEVCの厳密な構文が必要な時の入口。本文未確認なので今回の読了経路には入れない。
- 読む目的：解説・エンコーダ実装・規範文書を混同しないための一次参照先。通読の推奨ではなく疑問点を引くための候補。
- 確認範囲：書誌・公開状態・目次/要約/PDFへのリンクのみ。規格PDF本文、構文/意味対、規範的復号手続は未確認。
- 限界：概念項目は読む目的であって今回本文から実証した内容ではない。承認日とWeb掲載日を混同しない。

## IC04：High Efficiency Video Coding (HEVC): Algorithms and Architectures

- 出典：[書誌/公開資料](https://link.springer.com/book/10.1007/978-3-319-06895-4)。Vivienne Sze, Madhukar Budagavi, Gary J. Sullivan (eds.), Springer, 1st edition, 2014, DOI: 10.1007/978-3-319-06895-4
- 判定：**保留**。ハードウェア設計の不足を示すが章本文未確認。目次だけで具体的な章の理解成果を保証しない。
- 読む目的：規格の道具とハードウェア設計を橋渡しする参照書候補。章本文確認前の仮選定。
- 確認範囲：出版社の書誌・紹介・目次。章本文は未読であり、アーキテクチャ・ブロック分割・フィルタ本文を確認済みとは扱わない。
- 限界：出版社ページは公開されているが書籍全文は購読コンテンツ。全候補が無料全文という意味ではない。HEVCへの偏りを残す候補でもある。

## IC05：Compression Efficiency and Delay Tradeoffs for Hierarchical B-Pictures and Pulsed-Quality Frames

- 出典：[書誌/公開資料](https://doi.org/10.1109/tip.2007.896681)。Athanasios Leontaris and Pamela C. Cosman, IEEE Transactions on Image Processing, 16(7), 1726–1740, July 2007, DOI: 10.1109/TIP.2007.896681
- 判定：**目的限定参照**。P16の未来参照設計とは別に、入力待ちと出力バッファによる遅延を学ぶ時に参照。現在の性能順位には使わない。
- 読む目的：時間制約を、単なるエンコードfpsではなく入力待ち・出力バッファ・参照構造・ビット配分の問題として扱う。
- 確認範囲：機関リポジトリ表紙、要旨、序論と初期本文。全実験・数式導出・結果の再計算は未実施。
- 限界：H.264時代の研究。提示された遅延目標や比較優劣を現在の全用途に一般化しない。

## IC06：x265 Documentation — Preset Options

- 出典：[書誌/公開資料](https://x265.readthedocs.io/en/stable/presets.html)。x265 project documentation, stable branch, Web documentation
- 判定：**目的限定参照**。P08/P10のpreset差を読む時に実装文書へ接続。速いpresetとzerolatencyを区別する。
- 読む目的：論文の概念を、実際のエンコーダの探索量・評価設定・待ち行列の設定に接続する。
- 確認範囲：プリセット表、品質/速度の説明、psnr/ssim tune説明、zerolatencyの設定とframe threadsの遅延説明を確認。コード・実機動作・VBV節の本文は未検証。stableの特定リリース/コミット対応は未確定。
- 限界：可変なstable URLの取得時スナップショットであり版固定資料ではない。文書のzero latencyをネットワークを含む全系の遅延ゼロという保証に読まない。

## IC07：The Bjøntegaard Bible: Why your Way of Comparing Video Codecs May Be Wrong

- 出典：[書誌/公開資料](https://arxiv.org/html/2304.12852v2)。Christian Herglotz et al., arXiv:2304.12852v2, 22 December 2023
- 判定：**維持**。既存P13と同一論文。BD比較の時だけ戻る方針を維持。今回の候補生成は問題検索由来。
- 読む目的：圧縮性能の単一数値を読む前に、補間・比較区間・品質尺度・誤差の条件を監査する。
- 確認範囲：上記選択本文を確認。全表・全データセット・補間コードの実行は未確認。確認版はv2であり最終雑誌版と同一とは主張しない。
- 限界：論文名のBibleは必読合意を意味しない。論文の推奨や誤差量を全データセットに普遍化しない。

## IC08：Remote expert viewing, laboratory tests or objective metrics: which one(s) to trust?

- 出典：[書誌/公開資料](https://link.springer.com/article/10.1186/s13640-024-00630-7)。M. Wien and J. Jung, EURASIP Journal on Image and Video Processing, 2024, article 16, version of record 17 June 2024, DOI: 10.1186/s13640-024-00630-7
- 判定：**目的限定参照**。P15の理論とは違う、動画の対比較・視聴者・信頼区間を扱う実証研究。知覚品質経路の評価側を補う。
- 読む目的：平均指標での全体順位、同一映像内の方式差、専門家と一般視聴者の判定を区別する。
- 確認範囲：上記選択本文と書誌のみ。全プロトコル・統計計算・全実験を独立再検証したものではない。図は視覚確認していない。
- 限界：検証対象とプロトコルに依存する研究であり最良指標の普遍ランキングではない。要旨が明記するとおりBD-rateの複数レート集約自体は対象外。

検索式・発見後の書誌確認・読む条件は [independent-review.json](independent-review.json)。候補の一致数を選定の正しさの点数にはしない。
