<!-- このファイルは scripts/catalog.py により自動生成されます。直接編集しないでください。 -->

# 注釈付き文献一覧

リリース：selection-and-maintenance-2

範囲：目的別の文献地図。20論文＋3補助資料。体系的探索の一巡であり、最新網羅や普遍的な必読順位ではない。

`prerequisites` は必須依存関係ではなく、推奨学習順を表します。

## [P01](<papers/P01.md>) — Overview of the H.264/AVC Video Coding Standard

- 著者：Thomas Wiegand; Gary J. Sullivan; Gisle Bjøntegaard; Ajay Luthra
- 年・版：2003 / IEEE TCSVT
- 識別子：10.1109/TCSVT.2003.815165
- 論文：[公開ページ](<https://www.cs.ubc.ca/~krasic/cpsc538a/papers/h264avc-overview.pdf>)
- 分類：従来型 / 全体像 / 共通導入
- 役割：全体像
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：ハイブリッド符号化の各部品と、規格が決める範囲を理解する。
- 読む問い：規格で規定される復号過程と、自由に最適化できる符号化過程の境界はどこか。
- 他の候補との差：P03より古く簡潔な設計を足場にできる。
- 推奨学習順（必須依存ではない）：なし
- 必要な背景知識：基本的な確率・信号処理の用語
- 限界・注意：古い規格の概説であり、現在の最良実装・速度を代表しない。
- 根拠の確認範囲：本文抜粋確認 — Abstract; Introduction; Applications and Design Feature Highlights
- 根拠資料：[原文](<https://www.cs.ubc.ca/~krasic/cpsc538a/papers/h264avc-overview.pdf>)
- 読書状態：候補・利用者未読状態は未確認
- 個別根拠：規格はビットストリームの構文・制約と復号過程を規定し、符号化側の最適化には自由度を残す。（指定本文箇所確認、Introduction; Fig.1、[原文](<https://www.cs.ubc.ca/~krasic/cpsc538a/papers/h264avc-overview.pdf>)）
- 個別根拠：符号化層VCLとネットワーク抽象化層NALを分けて説明する。両者を圧縮アルゴリズムと転送形式の同一問題として扱わない。（指定本文箇所確認、§II–III、[原文](<https://www.cs.ubc.ca/~krasic/cpsc538a/papers/h264avc-overview.pdf>)）
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：ハイブリッド符号化の各部品と、規格が決める範囲を理解する。
- 選定上の補完性・代替との関係：P03より古く簡潔な設計を足場にできる。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P02](<papers/P02.md>) — Overview of the High Efficiency Video Coding (HEVC) Standard

- 著者：Gary J. Sullivan; Jens-Rainer Ohm; Woo-Jin Han; Thomas Wiegand
- 年・版：2012 / IEEE TCSVT
- 識別子：10.1109/TCSVT.2012.2221191
- 論文：[公開ページ](<https://ieeexplore.ieee.org/document/6316136/>)
- 分類：従来型 / 全体像 / 目的別経路
- 役割：全体像
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：AVCからVVCへ移る際の中間世代を把握する。
- 読む問い：圧縮効率改善のため、どの設計の自由度を増やしたのか。
- 他の候補との差：P01/P03間の系譜を埋め、HEVC比較論文の用語を理解できる。
- 推奨学習順（必須依存ではない）：[P01](<papers/P01.md>)
- 必要な背景知識：基本的な確率・信号処理の用語
- 限界・注意：今回は出版社の要旨・書誌を確認。個別ツールの詳細は本文未確認。
- 根拠の確認範囲：要旨・書誌確認 — IEEE Abstract / Metadata
- 根拠資料：[原文](<https://ieeexplore.ieee.org/document/6316136/>)
- 読書状態：候補・利用者未読状態は未確認
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：AVCからVVCへ移る際の中間世代を把握する。
- 選定上の補完性・代替との関係：P01/P03間の系譜を埋め、HEVC比較論文の用語を理解できる。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P03](<papers/P03.md>) — Overview of the Versatile Video Coding (VVC) Standard and its Applications

- 著者：Benjamin Bross; Ye-Kui Wang; Yan Ye; Shan Liu; Jianle Chen; Gary J. Sullivan; Jens-Rainer Ohm
- 年・版：2021 / IEEE TCSVT
- 識別子：https://www.microsoft.com/en-us/research/publication/overview-of-the-versatile-video-coding-vvc-standard-and-its-applications/
- 論文：[公開ページ](<https://www.microsoft.com/en-us/research/publication/overview-of-the-versatile-video-coding-vvc-standard-and-its-applications/>)
- 分類：従来型 / 全体像 / 目的別経路
- 役割：全体像
- 発見経路：前回答の多様な種
- 読む理由：現代的ハイブリッド方式の機能と用途を俯瞰する。
- 読む問い：用途の多様化はどの符号化ツールや制約に結び付くか。
- 他の候補との差：P04と対にし、単一の標準化系統に偏らない地図を作れる。
- 推奨学習順（必須依存ではない）：[P01](<papers/P01.md>)
- 必要な背景知識：基本的な確率・信号処理の用語
- 限界・注意：要旨中の削減率を普遍的性能差にしない。VTMと実用実装を区別する。
- 根拠の確認範囲：要旨・書誌確認 — Microsoft Research publication page / abstract
- 根拠資料：[原文](<https://www.microsoft.com/en-us/research/publication/overview-of-the-versatile-video-coding-vvc-standard-and-its-applications/>)
- 読書状態：候補・利用者未読状態は未確認
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：現代的ハイブリッド方式の機能と用途を俯瞰する。
- 選定上の補完性・代替との関係：P04と対にし、単一の標準化系統に偏らない地図を作れる。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P04](<papers/P04.md>) — A Technical Overview of AV1

- 著者：Jingning Han et al.
- 年・版：2021 / arXiv v2（初版2020）
- 識別子：arXiv:2008.06091
- 論文：[公開ページ](<https://arxiv.org/abs/2008.06091>)
- 分類：従来型 / 別系統 / 目的別経路
- 役割：別系統
- 発見経路：前回答の多様な種
- 読む理由：別の標準化系統とハードウェア実現性の視点を導入する。
- 読む問い：似た予測・変換構造でも、どの設計選択が異なるか。
- 他の候補との差：P03の単なる代替でなく、設計対比の相手。
- 推奨学習順（必須依存ではない）：[P01](<papers/P01.md>)
- 必要な背景知識：基本的な確率・信号処理の用語
- 限界・注意：今回確認したのはarXiv v2の要旨。最新AV1実装の性能を示す資料ではない。
- 根拠の確認範囲：要旨・書誌確認 — arXiv v2 abstract / submission history
- 根拠資料：[原文](<https://arxiv.org/abs/2008.06091>)
- 読書状態：候補・利用者未読状態は未確認
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：別の標準化系統とハードウェア実現性の視点を導入する。
- 選定上の補完性・代替との関係：P03の単なる代替でなく、設計対比の相手。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P05](<papers/P05.md>) — Context-Based Adaptive Binary Arithmetic Coding in the H.264/AVC Video Compression Standard

- 著者：Detlev Marpe; Heiko Schwarz; Thomas Wiegand
- 年・版：2003 / IEEE TCSVT
- 識別子：10.1109/TCSVT.2003.815173
- 論文：[公開ページ](<https://iphome.hhi.de/marpe/download/cabac_ieee03.pdf>)
- 分類：従来型 / 原理 / 目的別経路
- 役割：原理
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：確率モデル・二値化・算術符号化の役割を分離して理解する。
- 読む問い：コンテキストを良くすることと符号器を良くすることはどう違うか。
- 他の候補との差：概説だけでは見えにくいエントロピー符号化を掘り下げる。
- 推奨学習順（必須依存ではない）：[P01](<papers/P01.md>)
- 必要な背景知識：基本的な確率・信号処理の用語
- 限界・注意：二段組PDF抽出の列混在あり。数式・擬似コードは元PDFで再確認する。
- 根拠の確認範囲：本文抜粋確認 — Abstract / Introduction
- 根拠資料：[原文](<https://iphome.hhi.de/marpe/download/cabac_ieee03.pdf>)
- 読書状態：候補・利用者未読状態は未確認
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：確率モデル・二値化・算術符号化の役割を分離して理解する。
- 選定上の補完性・代替との関係：概説だけでは見えにくいエントロピー符号化を掘り下げる。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P06](<papers/P06.md>) — Rate-Distortion Optimization for Video Compression

- 著者：Gary J. Sullivan; Thomas Wiegand
- 年・版：1998 / IEEE Signal Processing Magazine
- 識別子：10.1109/79.733497
- 論文：[公開ページ](<https://web.stanford.edu/class/ee398a/handouts/papers/Sullivan%20-%20RD%20Opt%20for%20Video.pdf>)
- 分類：基礎 / 原理 / 共通導入
- 役割：原理
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：圧縮率と誤差の交換条件を符号化意思決定として理解する。
- 読む問い：予測誤差を最小にするだけでは、なぜ最良の符号化にならないのか。
- 他の候補との差：P05の確率モデルとは別に、モードやビット配分を選ぶ原理を補う。
- 推奨学習順（必須依存ではない）：[P01](<papers/P01.md>)
- 必要な背景知識：基本的な確率・信号処理の用語
- 限界・注意：過去のコーデックでの実験を最新性能に外挿しない。量子化・確率・最適化の基礎は別途必要。
- 根拠の確認範囲：本文抜粋確認 — Opening / Variable Block Sizes / Fig.3–4 discussion
- 根拠資料：[原文](<https://web.stanford.edu/class/ee398a/handouts/papers/Sullivan%20-%20RD%20Opt%20for%20Video.pdf>)
- 読書状態：候補・利用者未読状態は未確認
- 個別根拠：動き表現と残差符号化の選択は相互作用する。予測誤差だけでなく、モードや動きに費やすビットも含めて最適化する。（指定本文箇所確認、Video Compression Basics; Variable Block Sizes、[原文](<https://web.stanford.edu/class/ee398a/handouts/papers/Sullivan%20-%20RD%20Opt%20for%20Video.pdf>)）
- 個別根拠：ブロックサイズの例では小さいブロックの細かな予測と、動き表現の符号量の交換条件を示す。大きな自由度が常に無償の改善になるわけではない。（指定本文箇所確認、Variable Block Sizes; Fig.3–4、[原文](<https://web.stanford.edu/class/ee398a/handouts/papers/Sullivan%20-%20RD%20Opt%20for%20Video.pdf>)）
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：圧縮率と誤差の交換条件を符号化意思決定として理解する。
- 選定上の補完性・代替との関係：P05の確率モデルとは別に、モードやビット配分を選ぶ原理を補う。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P07](<papers/P07.md>) — Variational Image Compression with a Scale Hyperprior

- 著者：Johannes Ballé; David Minnen; Saurabh Singh; Sung Jin Hwang; Nick Johnston
- 年・版：2018 / ICLR
- 識別子：arXiv:1802.01436
- 論文：[公開ページ](<https://research.google/pubs/variational-image-compression-with-a-scale-hyperprior/>)
- 分類：学習型基礎 / 原理 / 目的別経路
- 役割：原理
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：学習型映像符号化の前提となる潜在表現と副情報を理解する。
- 読む問い：副情報を送るコストを払っても、なぜ全体の符号量を減らせるのか。
- 他の候補との差：P08/P10に入る前の画像符号化・確率モデルの橋渡し。
- 推奨学習順（必須依存ではない）：[P06](<papers/P06.md>)
- 必要な背景知識：基本的な確率・信号処理の用語, ニューラルネットワークの基礎, 量子化と確率モデルの区別
- 限界・注意：画像圧縮の論文。時間方向の予測や長系列安定性を解いたとは扱わない。
- 根拠の確認範囲：本文の構造・符号化順序・評価上の注意を確認 — arXiv v2 §2–3; Fig.2–4; §4.2 Fig.5/7; §5
- 根拠資料：[原文](<https://arxiv.org/html/1802.01436v2>)
- 読書状態：候補・利用者未読状態は未確認
- 個別根拠：量子化したhyperlatent zを副情報として先に復号し、予測した尺度を使って画像latent yの確率を得て復号する。副情報の費用も損失に含む。（指定本文箇所確認、§3; Eq.10; Fig.3–4、[原文](<https://arxiv.org/html/1802.01436v2>)）
- 個別根拠：factorized priorに残る依存を尺度で説明する設計であり、画像latentの全依存を完全に消したとの保証ではない。（指定本文箇所確認、§2 Fig.2; §3; §5、[原文](<https://arxiv.org/html/1802.01436v2>)）
- 個別根拠：Fig.5のPSNR曲線は等lambda、MS-SSIM曲線は補間した等rateで集約する。学習損失と評価指標・集約条件を分けて読む。（指定本文箇所確認、§4.2; Fig.5 caption、[原文](<https://arxiv.org/html/1802.01436v2>)）
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：学習型映像符号化の前提となる潜在表現と副情報を理解する。
- 選定上の補完性・代替との関係：P08/P10に入る前の画像符号化・確率モデルの橋渡し。
- 確信度：符号化順序と費用を本文で確認し、概念教材としての根拠を補強。影響度の定量評価は未実施。

## [P08](<papers/P08.md>) — DVC: An End-To-End Deep Video Compression Framework

- 著者：Guo Lu; Wanli Ouyang; Dong Xu; Xiaoyun Zhang; Chunlei Cai; Zhiyong Gao
- 年・版：2019 / CVPR
- 識別子：https://openaccess.thecvf.com/content_CVPR_2019/html/Lu_DVC_An_End-To-End_Deep_Video_Compression_Framework_CVPR_2019_paper.html
- 論文：[公開ページ](<https://openaccess.thecvf.com/content_CVPR_2019/html/Lu_DVC_An_End-To-End_Deep_Video_Compression_Framework_CVPR_2019_paper.html>)
- 分類：学習型 / 転換点 / 目的別経路
- 役割：転換点
- 発見経路：前回答の多様な種
- 読む理由：動き・残差を学習器で符号化する構造を従来型と対応させる。
- 読む問い：従来の予測構造を残しつつ、何を共同最適化したのか。
- 他の候補との差：P10との対比に必要な残差符号化側の足場。
- 推奨学習順（必須依存ではない）：[P01](<papers/P01.md>), [P06](<papers/P06.md>), [P07](<papers/P07.md>)
- 必要な背景知識：基本的な確率・信号処理の用語, ニューラルネットワークの基礎, 量子化と確率モデルの区別
- 限界・注意：主結果は特定のFFmpeg設定。別実装・presetへの優位性に拡張しない。
- 根拠の確認範囲：本文の構造・実験条件確認 — CVPR paper §3; §4.1–4.2
- 根拠資料：[原文](<https://openaccess.thecvf.com/content_CVPR_2019/papers/Lu_DVC_An_End-To-End_Deep_Video_Compression_Framework_CVPR_2019_paper.pdf>)
- 読書状態：候補・利用者未読状態は未確認
- 個別根拠：動き推定・補償と、動き／残差の表現を用いる構造を共同のRD損失で学習する。従来型との部品対応を示す。（指定本文箇所確認、§3.2; Fig.2; §3.6、[原文](<https://openaccess.thecvf.com/content_CVPR_2019/papers/Lu_DVC_An_End-To-End_Deep_Video_Compression_Framework_CVPR_2019_paper.pdf>)）
- 個別根拠：本文の従来型比較はFFmpeg very fast mode、GOPはUVG=12、HEVC=10。普遍的な規格間性能差ではない。（指定本文箇所確認、§4.1–4.2、[原文](<https://openaccess.thecvf.com/content_CVPR_2019/papers/Lu_DVC_An_End-To-End_Deep_Video_Compression_Framework_CVPR_2019_paper.pdf>)）
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：動き・残差を学習器で符号化する構造を従来型と対応させる。
- 選定上の補完性・代替との関係：P10との対比に必要な残差符号化側の足場。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P09](<papers/P09.md>) — Scale-Space Flow for End-to-End Optimized Video Compression

- 著者：Eirikur Agustsson; David Minnen; Nick Johnston; Johannes Ballé; Sung Jin Hwang; George Toderici
- 年・版：2020 / CVPR
- 識別子：https://openaccess.thecvf.com/content_CVPR_2020/html/Agustsson_Scale-Space_Flow_for_End-to-End_Optimized_Video_Compression_CVPR_2020_paper.html
- 論文：[公開ページ](<https://openaccess.thecvf.com/content_CVPR_2020/html/Agustsson_Scale-Space_Flow_for_End-to-End_Optimized_Video_Compression_CVPR_2020_paper.html>)
- 分類：学習型 / 別設計 / 目的別経路
- 役割：別設計
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：動き予測の不確実性と学習手順の単純化を見る。
- 読む問い：隠れていた領域の出現や速い動きを、通常のワーピングからどう改善するか。
- 他の候補との差：残差→条件付けだけでない設計軸をP08に追加する。
- 推奨学習順（必須依存ではない）：[P08](<papers/P08.md>)
- 必要な背景知識：基本的な確率・信号処理の用語
- 限界・注意：要旨は低遅延・Bフレームなしと記載。詳しい実験設定と性能は未監査。
- 根拠の確認範囲：要旨・書誌確認 — CVF abstract
- 根拠資料：[原文](<https://openaccess.thecvf.com/content_CVPR_2020/html/Agustsson_Scale-Space_Flow_for_End-to-End_Optimized_Video_Compression_CVPR_2020_paper.html>)
- 読書状態：候補・利用者未読状態は未確認
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：動き予測の不確実性と学習手順の単純化を見る。
- 選定上の補完性・代替との関係：残差→条件付けだけでない設計軸をP08に追加する。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P10](<papers/P10.md>) — Deep Contextual Video Compression

- 著者：Jiahao Li; Bin Li; Yan Lu
- 年・版：2021 / NeurIPS
- 識別子：arXiv:2109.15047
- 論文：[公開ページ](<https://proceedings.neurips.cc/paper_files/paper/2021/hash/96b250a90d3cf0868c83f8c965142d2a-Abstract.html>)
- 分類：学習型 / 転換点 / 目的別経路
- 役割：転換点
- 発見経路：前回答の多様な種
- 読む理由：残差を固定的に作る設計から、特徴の条件付けへ比較する。
- 読む問い：条件情報をencoder・decoder・entropy modelのどこでどう使うのか。
- 他の候補との差：P08からの概念差を学ぶ。小さな性能差だけを選定理由にしない。
- 推奨学習順（必須依存ではない）：[P07](<papers/P07.md>), [P08](<papers/P08.md>)
- 必要な背景知識：基本的な確率・信号処理の用語, ニューラルネットワークの基礎, 量子化と確率モデルの区別
- 限界・注意：DVC原著と比較条件が異なる。著者らによる同条件での再評価と原著値を区別する。
- 根拠の確認範囲：本文の構造・実験条件確認 — NeurIPS paper §3–4.2
- 根拠資料：[原文](<https://proceedings.neurips.cc/paper_files/paper/2021/file/96b250a90d3cf0868c83f8c965142d2a-Paper.pdf>)
- 読書状態：候補・利用者未読状態は未確認
- 個別根拠：特徴空間のcontextをencoder、decoder、entropy modelに与える。単に残差画像を別名で送る設計ではない。（指定本文箇所確認、§3.1–3.3; Fig.1–2、[原文](<https://proceedings.neurips.cc/paper_files/paper/2021/file/96b250a90d3cf0868c83f8c965142d2a-Paper.pdf>)）
- 個別根拠：context learningは再構成参照と符号化された動きを使う。受信側が原フレームを無料で参照するわけではない。（指定本文箇所確認、§3.3、[原文](<https://proceedings.neurips.cc/paper_files/paper/2021/file/96b250a90d3cf0868c83f8c965142d2a-Paper.pdf>)）
- 個別根拠：DVC/DVCProを同じintra codecで再評価し、x264/x265はveryslowとconstant QPで比較する。DVC原著値と混ぜない。（指定本文箇所確認、§4.1–4.2、[原文](<https://proceedings.neurips.cc/paper_files/paper/2021/file/96b250a90d3cf0868c83f8c965142d2a-Paper.pdf>)）
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：残差との対比に有用。ただし学習型の発展をDVC→DCVCという唯一の系譜で説明しない。P18を別系統として併読。
- 選定上の補完性・代替との関係：P08からの概念差を学ぶ。小さな性能差だけを選定理由にしない。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P11](<papers/P11.md>) — NeRV: Neural Representations for Videos

- 著者：Hao Chen; Bo He; Hanyu Wang; Yixuan Ren; Ser Nam Lim; Abhinav Shrivastava
- 年・版：2021 / NeurIPS
- 識別子：arXiv:2110.13903
- 論文：[公開ページ](<https://neurips.cc/virtual/2021/poster/26386>)
- 分類：動画別表現 / 別設計 / 目的別経路
- 役割：別設計
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：動画をモデル重みとして表す別の符号化観を導入する。
- 読む問い：符号化を動画ごとの最適化に置き換えると、どのコストが移動するか。
- 他の候補との差：汎用モデルによる逐次符号化のP08/P10とは違う枝。
- 推奨学習順（必須依存ではない）：[P06](<papers/P06.md>), [P07](<papers/P07.md>)
- 必要な背景知識：基本的な確率・信号処理の用語, ニューラルネットワークの基礎, 量子化と確率モデルの区別
- 限界・注意：学習・適合時間と重みの符号量を要確認。実時間ストリーミングと同じ条件ではない。
- 根拠の確認範囲：要旨・書誌確認 — NeurIPS poster abstract
- 根拠資料：[原文](<https://neurips.cc/virtual/2021/poster/26386>)
- 読書状態：候補・利用者未読状態は未確認
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：動画をモデル重みとして表す別の符号化観を導入する。
- 選定上の補完性・代替との関係：汎用モデルによる逐次符号化のP08/P10とは違う枝。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P12](<papers/P12.md>) — Towards Practical Real-Time Neural Video Compression

- 著者：Zhaoyang Jia; Bin Li; Jiahao Li; Wenxuan Xie; Linfeng Qi; Houqiang Li; Yan Lu
- 年・版：2025 / CVPR
- 識別子：arXiv:2502.20762
- 論文：[公開ページ](<https://openaccess.thecvf.com/content/CVPR2025/html/Jia_Towards_Practical_Real-Time_Neural_Video_Compression_CVPR_2025_paper.html>)
- 分類：学習型 / 実装制約 / 目的別経路
- 役割：実装制約
- 発見経路：前回答の多様な種
- 読む理由：圧縮率以外の実装コストとデバイス間整合性を読む。
- 読む問い：演算量削減だけで速度が上がるか。整数化すると何を失い何を得るか。
- 他の候補との差：P10系統の後続を、単なるRD改善でなく実用性の観点で選定する。
- 推奨学習順（必須依存ではない）：[P10](<papers/P10.md>), [P13](<papers/P13.md>), [P14](<papers/P14.md>)
- 必要な背景知識：基本的な確率・信号処理の用語, ニューラルネットワークの基礎, 量子化と確率モデルの区別
- 限界・注意：A100・fp16の値を全GPUやint16に流用しない。コードの実行再現は未実施。
- 根拠の確認範囲：本文の構造・実験条件確認 — CVPR paper §5.1; Tables 2–3; Fig.5(c)
- 根拠資料：[原文](<https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Towards_Practical_Real-Time_Neural_Video_Compression_CVPR_2025_paper.pdf>)
- 読書状態：候補・利用者未読状態は未確認
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：圧縮率以外の実装コストとデバイス間整合性を読む。
- 選定上の補完性・代替との関係：P10系統の後続を、単なるRD改善でなく実用性の観点で選定する。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P13](<papers/P13.md>) — The Bjøntegaard Bible: Why your Way of Comparing Video Codecs May Be Wrong

- 著者：Christian Herglotz et al.
- 年・版：2023 / arXiv v2（受理記載あり）
- 識別子：arXiv:2304.12852
- 論文：[公開ページ](<https://arxiv.org/html/2304.12852>)
- 分類：評価 / 評価批判 / 評価時に参照
- 役割：評価批判
- 発見経路：前回答の多様な種
- 読む理由：BD値を読む際の補間・区間・測定誤差を学ぶ。
- 読む問い：小さなBD差を本当の改善と判断するには何を確認するか。
- 他の候補との差：手法提案のP08/P10/P12とは役割が異なり、比較の誤読を抑える。
- 推奨学習順（必須依存ではない）：[P06](<papers/P06.md>)
- 必要な背景知識：基本的な確率・信号処理の用語
- 限界・注意：今回は要旨・導入を中心に確認。全数値実験の検算は未実施。
- 根拠の確認範囲：本文抜粋確認 — arXiv v2 Abstract / Introduction
- 根拠資料：[原文](<https://arxiv.org/html/2304.12852>)
- 読書状態：候補・利用者未読状態は未確認
- 個別根拠：BD計算の補間誤差を検討し、相対曲線差の確認や差の大きさに応じた慎重な解釈を推奨する。（要旨・導入確認、Abstract; Introduction、[原文](<https://arxiv.org/html/2304.12852>)）
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：BD値を読む際の補間・区間・測定誤差を学ぶ。
- 選定上の補完性・代替との関係：手法提案のP08/P10/P12とは役割が異なり、比較の誤読を抑える。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P14](<papers/P14.md>) — The Practice of Averaging Rate-Distortion Curves over Testsets to Compare Learned Video Codecs Can Cause Misleading Conclusions

- 著者：M. Akin Yilmaz; Onur Keleş; A. Murat Tekalp
- 年・版：2024 / arXiv v2
- 識別子：arXiv:2409.08772
- 論文：[公開ページ](<https://arxiv.org/html/2409.08772>)
- 分類：評価 / 評価批判 / 評価時に参照
- 役割：評価批判
- 発見経路：前回答の多様な種
- 読む理由：データ集合の集約順序による結論の変化を理解する。
- 読む問い：平均RD曲線とシーケンス別BD値の平均はなぜ違うのか。
- 他の候補との差：P13の補間問題とは異なる集約の問題を補う。
- 推奨学習順（必須依存ではない）：[P13](<papers/P13.md>)
- 必要な背景知識：基本的な確率・信号処理の用語
- 限界・注意：特定比較の例を全学習型研究の誤りと一般化しない。重み付けの目的も明示する。
- 根拠の確認範囲：本文抜粋確認 — arXiv v2 Abstract / §1–2 / references
- 根拠資料：[原文](<https://arxiv.org/html/2409.08772>)
- 読書状態：候補・利用者未読状態は未確認
- 個別根拠：平均RD曲線から計算したBDとシーケンス別BDの平均が異なる結論を与え得ることを、解析と動画codec比較の例で示す。全データ集合で必ず逆転するという主張ではない。（要旨・導入確認、Abstract; §1–2、[原文](<https://arxiv.org/html/2409.08772>)）
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：データ集合の集約順序による結論の変化を理解する。
- 選定上の補完性・代替との関係：P13の補間問題とは異なる集約の問題を補う。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P15](<papers/P15.md>) — Rethinking Lossy Compression: The Rate-Distortion-Perception Tradeoff

- 著者：Yochai Blau; Tomer Michaeli
- 年・版：2019 / ICML / PMLR 97
- 識別子：arXiv:1901.07821
- 論文：[公開ページ](<https://proceedings.mlr.press/v97/blau19a.html>)
- 分類：知覚・理論 / 原理 / 目的別経路
- 役割：原理
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：低歪みと知覚的自然さを別の目標として理解する。
- 読む問い：忠実性・符号量・知覚品質を同時に改善できる範囲は何か。
- 他の候補との差：PSNR中心の比較に対し、目的そのものを問い直す。
- 推奨学習順（必須依存ではない）：[P06](<papers/P06.md>)
- 必要な背景知識：基本的な確率・信号処理の用語
- 限界・注意：画像・理論の基礎資料。動画の時間的一貫性や主観品質を直接保証するものではない。
- 根拠の確認範囲：要旨・書誌確認 — PMLR abstract / citation metadata
- 根拠資料：[原文](<https://proceedings.mlr.press/v97/blau19a.html>)
- 読書状態：候補・利用者未読状態は未確認
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：低歪みと知覚的自然さを別の目標として理解する。
- 選定上の補完性・代替との関係：PSNR中心の比較に対し、目的そのものを問い直す。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P16](<papers/P16.md>) — End-to-End Rate-Distortion Optimized Learned Hierarchical Bi-Directional Video Compression

- 著者：M. Akın Yılmaz; A. Murat Tekalp
- 年・版：2021 / arXiv v1（TIP受理記載；刊行版との差分未確認）
- 識別子：arXiv:2112.09529
- 論文：[公開ページ](<https://arxiv.org/abs/2112.09529>)
- 分類：学習型 / 別設計 / 目的別経路
- 役割：別設計
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：低遅延だけに偏らず、階層的双方向予測を扱う。
- 読む問い：未来フレームを使えると圧縮率・遅延・参照構造はどう変わるか。
- 他の候補との差：P09/P10の逐次的条件と異なる時間構造を補う。
- 推奨学習順（必須依存ではない）：[P08](<papers/P08.md>)
- 必要な背景知識：基本的な確率・信号処理の用語
- 限界・注意：要旨のx265/SVT-HEVC/HMへの主張を、低遅延方式との公平な順位に使わない。
- 根拠の確認範囲：要旨・書誌確認 — arXiv v1 abstract / acceptance comment
- 根拠資料：[原文](<https://arxiv.org/abs/2112.09529>)
- 読書状態：候補・利用者未読状態は未確認
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：低遅延だけに偏らず、階層的双方向予測を扱う。
- 選定上の補完性・代替との関係：P09/P10の逐次的条件と異なる時間構造を補う。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P17](<papers/P17.md>) — Deep Learning-Based Video Coding: A Review and A Case Study

- 著者：Dong Liu; Yue Li; Jianping Lin; Houqiang Li; Feng Wu
- 年・版：2020 / ACM Computing Surveys（確認資料はarXiv 2019 v1の要旨・書誌）
- 識別子：10.1145/3368405
- 論文：[公開ページ](<https://arxiv.org/abs/1904.12462>)
- 分類：学習・従来混合 / 全体像 / 目的別経路
- 役割：全体像
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：学習型の新方式と、既存方式への学習ツール組込みを分ける。
- 読む問い：規格や既存構造を維持しながら、どの部分を学習器にできるか。
- 他の候補との差：エンドツーエンド論文だけに偏る候補集合を補正する。
- 推奨学習順（必須依存ではない）：[P01](<papers/P01.md>)
- 必要な背景知識：基本的な確率・信号処理の用語
- 限界・注意：歴史的サーベイであり最新動向ではない。複数ツールを組み合わせた利得を一つの部品の効果にしない。
- 根拠の確認範囲：要旨・書誌確認 — arXiv abstract / journal reference
- 根拠資料：[原文](<https://arxiv.org/abs/1904.12462>)
- 読書状態：候補・利用者未読状態は未確認
- 選定判断：維持（目的別の読む役割を限定）
- 重要性：学習型の新方式と、既存方式への学習ツール組込みを分ける。
- 選定上の補完性・代替との関係：エンドツーエンド論文だけに偏る候補集合を補正する。
- 確信度：選定理由は編集上の判断。分野全体の必読合意や引用数順位は未検証。

## [P18](<papers/P18.md>) — Learned Video Compression

- 著者：Oren Rippel; Sanjay Nair; Carissa Lew; Steve Branson; Alexander G. Anderson; Lubomir Bourdev
- 年・版：2019 / ICCV 2019
- 識別子：https://openaccess.thecvf.com/content_ICCV_2019/html/Rippel_Learned_Video_Compression_ICCV_2019_paper.html
- 論文：[公開ページ](<https://openaccess.thecvf.com/content_ICCV_2019/html/Rippel_Learned_Video_Compression_ICCV_2019_paper.html>)
- 分類：学習型 / 別設計 / 目的別経路
- 役割：別設計
- 発見経路：S03 §3.7で別系統として検討し、参考文献\[153\]を確認。初回発見はタイトル検索。
- 読む理由：学習した状態の伝播、動きと残差の共同表現、空間レート制御を別系統として読む。
- 読む問い：再構成フレームだけでなく状態を引き継ぐことで、何を表現でき、何を送る必要があるか。
- 他の候補との差：DVC→DCVCだけの系譜を補正する。性能順位ではなく状態・制御という設計軸を追加。
- 推奨学習順（必須依存ではない）：[P08](<papers/P08.md>)
- 必要な背景知識：P01で扱う基本構造, レート歪みの概念
- 限界・注意：当時のlow-latency条件の主張。全実験設定・現在の実装比較・再現は未確認。
- 根拠の確認範囲：本文の構造とレート制御節確認 — §2.1; §3; §4.1–4.2
- 根拠資料：[原文](<https://openaccess.thecvf.com/content_ICCV_2019/papers/Rippel_Learned_Video_Compression_ICCV_2019_paper.pdf>)
- 読書状態：候補・利用者の既読状態は未確認
- 個別根拠：一般化した学習状態を引き継ぎ、低帯域のbottleneckを通じて更新する。state-to-frameから再構成する。（指定本文箇所確認、§2.1; Fig.5、[原文](<https://openaccess.thecvf.com/content_ICCV_2019/papers/Rippel_Learned_Video_Compression_ICCV_2019_paper.pdf>)）
- 個別根拠：空間的な可変rateを扱う機構と、RD曲線の傾きを用いるrate controllerを分けて記述する。（指定本文箇所確認、§4.1–4.2、[原文](<https://openaccess.thecvf.com/content_ICCV_2019/papers/Rippel_Learned_Video_Compression_ICCV_2019_paper.pdf>)）
- 選定判断：追加（共通導入には追加しない）
- 重要性：学習した状態の伝播、動きと残差の共同表現、空間レート制御を別系統として読む。
- 選定上の補完性・代替との関係：DVC→DCVCだけの系譜を補正する。性能順位ではなく状態・制御という設計軸を追加。
- 確信度：§2.1/§4を確認し、別設計の教材として選定。全比較実験は未監査。

## [P19](<papers/P19.md>) — λ Domain Rate Control Algorithm for High Efficiency Video Coding

- 著者：Bin Li; Houqiang Li; Li Li; Jinlei Zhang
- 年・版：2014 / IEEE TIP 23(9), 3841–3854
- 識別子：10.1109/TIP.2014.2336550
- 論文：[公開ページ](<https://doi.org/10.1109/TIP.2014.2336550>)
- 分類：従来型 / レート制御 / 目的別経路
- 役割：レート制御
- 発見経路：レート制御の概念別検索→DOI取得失敗→Europe PMC APIの書誌・要旨に切替。
- 読む理由：モード選択のRDOと、目標ビットレートに合わせる制御を区別する入口。
- 読む問い：R-QモデルではなくR-lambdaモデルを用いる狙いは何か。
- 他の候補との差：従来型レート制御という未収集の枝を補う。ニューラル方式への置換ではない。
- 推奨学習順（必須依存ではない）：[P02](<papers/P02.md>), [P06](<papers/P06.md>)
- 必要な背景知識：P01で扱う基本構造, レート歪みの概念
- 限界・注意：出版社の本文取得に失敗。索引に収録された著者要旨のみ確認し、採用経緯・実装・数値は独立検証していない。
- 根拠の確認範囲：索引書誌・著者要旨確認 — Europe PMC MED:25020096 abstract / DOI metadata
- 根拠資料：[原文](<https://europepmc.org/article/MED/25020096>)
- 読書状態：候補・利用者の既読状態は未確認
- 個別根拠：著者要旨はRとlambdaの対応を使った制御、階層的bit allocation、HEVC参照ソフトへの統合を報告する。実装採用は著者報告として保持。（索引収録の著者要旨確認、Abstract、[原文](<https://europepmc.org/article/MED/25020096>)）
- 選定判断：追加（共通導入には追加しない）
- 重要性：モード選択のRDOと、目標ビットレートに合わせる制御を区別する入口。
- 選定上の補完性・代替との関係：従来型レート制御という未収集の枝を補う。ニューラル方式への置換ではない。
- 確信度：本文未取得。索引書誌・著者要旨に基づく仮候補。

## [P20](<papers/P20.md>) — Emerging Advances in Learned Video Compression: Models, Systems and Beyond

- 著者：Chuanmin Jia; Feng Ye; Siwei Ma; Wen Gao; Huifang Sun; Leonardo Chiariglione
- 年・版：2025 / IJCAI 2025 Survey Track, 10490–10498
- 識別子：10.24963/ijcai.2025/1165
- 論文：[公開ページ](<https://doi.org/10.24963/ijcai.2025/1165>)
- 分類：学習型 / 全体像 / 目的別経路
- 役割：全体像
- 発見経路：別著者・別年のサーベイを探すキーワード検索→IJCAI公式PDF。
- 読む理由：単方向/双方向、最適化、システム設計の分類から初期集合の抜けを探す。
- 読む問い：方式・時間条件・レート制御・ハードウェアを分離すると、どの研究枝が抜けているか。
- 他の候補との差：P17の2019版とは対象年代・範囲が違う。P17のhybrid tools分類を捨てずに地図を更新。
- 推奨学習順（必須依存ではない）：[P01](<papers/P01.md>)
- 必要な背景知識：P01で扱う基本構造, レート歪みの概念
- 限界・注意：サーベイ著者も関連研究に参加。別著者の視点ではあるが完全に中立な第三者ベンチマークとは扱わない。2026年網羅ではない。
- 根拠の確認範囲：本文の分類・システム・実験条件節確認 — §2–5; Table 1/3
- 根拠資料：[原文](<https://www.ijcai.org/proceedings/2025/1165.pdf>)
- 読書状態：候補・利用者の既読状態は未確認
- 個別根拠：分類は単方向/双方向予測に加え、rate control、model quantization、edge/mobile deploymentを含む。（指定本文箇所確認、§2–4、[原文](<https://www.ijcai.org/proceedings/2025/1165.pdf>)）
- 個別根拠：実験は先頭96フレーム、従来方式はRandom Access、LVCはintra-period/GOP=32。（指定本文箇所確認、§5 Test Conditions、[原文](<https://www.ijcai.org/proceedings/2025/1165.pdf>)）
- 個別根拠：本文の一部手法のPSNR比較ではVTMとの差を報告し、low-latencyやGOPによる結果の変化も述べる。普遍的な学習型優位とは読まない。（指定本文箇所確認、§5 Experimental Results、[原文](<https://www.ijcai.org/proceedings/2025/1165.pdf>)）
- 選定判断：追加（共通導入には追加しない）
- 重要性：単方向/双方向、最適化、システム設計の分類から初期集合の抜けを探す。
- 選定上の補完性・代替との関係：P17の2019版とは対象年代・範囲が違う。P17のhybrid tools分類を捨てずに地図を更新。
- 確信度：§2–5を確認し地図として選定。サーベイの網羅性・数値再現は未検証。
