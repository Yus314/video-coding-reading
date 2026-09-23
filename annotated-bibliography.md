# 注釈付き候補集合

初期版 initial-1 / 2026-09-23。注釈と読書順はassistantによる提案であり、利用者の読了・評価を推定していない。コード再現は全件未実施。未確認は論文に未記載という意味ではない。

## P01 — Overview of the H.264/AVC Video Coding Standard

- 著者：Thomas Wiegand; Gary J. Sullivan; Gisle Bjøntegaard; Ajay Luthra
- 年・版：2003 / IEEE TCSVT
- 識別子：10.1109/TCSVT.2003.815165
- 論文：[公開ページ](https://www.cs.ubc.ca/~krasic/cpsc538a/papers/h264avc-overview.pdf)
- 分類：従来型 / 全体像 / 共通導入
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：ハイブリッド符号化の各部品と、規格が決める範囲を理解する。
- 読む問い：**規格で規定される復号過程と、自由に最適化できる符号化過程の境界はどこか。**
- 他の候補との差：P03より古く簡潔な設計を足場にできる。
- 推奨前提：基本的な確率・信号処理の用語
- 限界・注意：古い規格の概説であり、現在の最良実装・速度を代表しない。
- 根拠の確認範囲：本文抜粋確認 — Abstract; Introduction; Applications and Design Feature Highlights
- 根拠：[原文](https://www.cs.ubc.ca/~krasic/cpsc538a/papers/h264avc-overview.pdf) / [元資料](https://www.cs.ubc.ca/~krasic/cpsc538a/papers/h264avc-overview.pdf)
- 状態：候補。利用者の既読状態は未確認。

## P02 — Overview of the High Efficiency Video Coding (HEVC) Standard

- 著者：Gary J. Sullivan; Jens-Rainer Ohm; Woo-Jin Han; Thomas Wiegand
- 年・版：2012 / IEEE TCSVT
- 識別子：10.1109/TCSVT.2012.2221191
- 論文：[公開ページ](https://ieeexplore.ieee.org/document/6316136/)
- 分類：従来型 / 全体像 / 分岐候補
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：AVCからVVCへ移る際の中間世代を把握する。
- 読む問い：**圧縮効率改善のため、どの設計の自由度を増やしたのか。**
- 他の候補との差：P01/P03間の系譜を埋め、HEVC比較論文の用語を理解できる。
- 推奨前提：P01
- 限界・注意：今回は出版社の要旨・書誌を確認。個別ツールの詳細は本文未確認。
- 根拠の確認範囲：要旨・書誌確認 — IEEE Abstract / Metadata
- 根拠：[原文](https://ieeexplore.ieee.org/document/6316136/) / [元資料](https://ieeexplore.ieee.org/document/6316136/)
- 状態：候補。利用者の既読状態は未確認。

## P03 — Overview of the Versatile Video Coding (VVC) Standard and its Applications

- 著者：Benjamin Bross; Ye-Kui Wang; Yan Ye; Shan Liu; Jianle Chen; Gary J. Sullivan; Jens-Rainer Ohm
- 年・版：2021 / IEEE TCSVT
- 識別子：https://www.microsoft.com/en-us/research/publication/overview-of-the-versatile-video-coding-vvc-standard-and-its-applications/
- 論文：[公開ページ](https://www.microsoft.com/en-us/research/publication/overview-of-the-versatile-video-coding-vvc-standard-and-its-applications/)
- 分類：従来型 / 全体像 / 分岐候補
- 発見経路：前回答の多様な種
- 読む理由：現代的ハイブリッド方式の機能と用途を俯瞰する。
- 読む問い：**用途の多様化はどの符号化ツールや制約に結び付くか。**
- 他の候補との差：P04と対にし、単一の標準化系統に偏らない地図を作れる。
- 推奨前提：P01
- 限界・注意：要旨中の削減率を普遍的性能差にしない。VTMと実用実装を区別する。
- 根拠の確認範囲：要旨・書誌確認 — Microsoft Research publication page / abstract
- 根拠：[原文](https://www.microsoft.com/en-us/research/publication/overview-of-the-versatile-video-coding-vvc-standard-and-its-applications/) / [元資料](https://www.microsoft.com/en-us/research/publication/overview-of-the-versatile-video-coding-vvc-standard-and-its-applications/)
- 状態：候補。利用者の既読状態は未確認。

## P04 — A Technical Overview of AV1

- 著者：Jingning Han et al.
- 年・版：2021 / arXiv v2（初版2020）
- 識別子：arXiv:2008.06091
- 論文：[公開ページ](https://arxiv.org/abs/2008.06091)
- 分類：従来型 / 別系統 / 分岐候補
- 発見経路：前回答の多様な種
- 読む理由：別の標準化系統とハードウェア実現性の視点を導入する。
- 読む問い：**似た予測・変換構造でも、どの設計選択が異なるか。**
- 他の候補との差：P03の単なる代替でなく、設計対比の相手。
- 推奨前提：P01
- 限界・注意：今回確認したのはarXiv v2の要旨。最新AV1実装の性能を示す資料ではない。
- 根拠の確認範囲：要旨・書誌確認 — arXiv v2 abstract / submission history
- 根拠：[原文](https://arxiv.org/abs/2008.06091) / [元資料](https://arxiv.org/abs/2008.06091)
- 状態：候補。利用者の既読状態は未確認。

## P05 — Context-Based Adaptive Binary Arithmetic Coding in the H.264/AVC Video Compression Standard

- 著者：Detlev Marpe; Heiko Schwarz; Thomas Wiegand
- 年・版：2003 / IEEE TCSVT
- 識別子：10.1109/TCSVT.2003.815173
- 論文：[公開ページ](https://iphome.hhi.de/marpe/download/cabac_ieee03.pdf)
- 分類：従来型 / 原理 / 分岐候補
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：確率モデル・二値化・算術符号化の役割を分離して理解する。
- 読む問い：**コンテキストを良くすることと符号器を良くすることはどう違うか。**
- 他の候補との差：概説だけでは見えにくいエントロピー符号化を掘り下げる。
- 推奨前提：P01
- 限界・注意：二段組PDF抽出の列混在あり。数式・擬似コードは元PDFで再確認する。
- 根拠の確認範囲：本文抜粋確認 — Abstract / Introduction
- 根拠：[原文](https://iphome.hhi.de/marpe/download/cabac_ieee03.pdf) / [元資料](https://iphome.hhi.de/marpe/download/cabac_ieee03.pdf)
- 状態：候補。利用者の既読状態は未確認。

## P06 — Rate-Distortion Optimization for Video Compression

- 著者：Gary J. Sullivan; Thomas Wiegand
- 年・版：1998 / IEEE Signal Processing Magazine
- 識別子：10.1109/79.733497
- 論文：[公開ページ](https://web.stanford.edu/class/ee398a/handouts/papers/Sullivan%20-%20RD%20Opt%20for%20Video.pdf)
- 分類：基礎 / 原理 / 共通導入
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：圧縮率と誤差の交換条件を符号化意思決定として理解する。
- 読む問い：**予測誤差を最小にするだけでは、なぜ最良の符号化にならないのか。**
- 他の候補との差：P05の確率モデルとは別に、モードやビット配分を選ぶ原理を補う。
- 推奨前提：P01
- 限界・注意：過去のコーデックでの実験を最新性能に外挿しない。量子化・確率・最適化の基礎は別途必要。
- 根拠の確認範囲：本文抜粋確認 — Opening / Variable Block Sizes / Fig.3–4 discussion
- 根拠：[原文](https://web.stanford.edu/class/ee398a/handouts/papers/Sullivan%20-%20RD%20Opt%20for%20Video.pdf) / [元資料](https://web.stanford.edu/class/ee398a/handouts/papers/Sullivan%20-%20RD%20Opt%20for%20Video.pdf)
- 状態：候補。利用者の既読状態は未確認。

## P07 — Variational Image Compression with a Scale Hyperprior

- 著者：Johannes Ballé; David Minnen; Saurabh Singh; Sung Jin Hwang; Nick Johnston
- 年・版：2018 / ICLR
- 識別子：arXiv:1802.01436
- 論文：[公開ページ](https://research.google/pubs/variational-image-compression-with-a-scale-hyperprior/)
- 分類：学習型基礎 / 原理 / 共通導入
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：学習型映像符号化の前提となる潜在表現と副情報を理解する。
- 読む問い：**副情報を送るコストを払っても、なぜ全体の符号量を減らせるのか。**
- 他の候補との差：P08/P10に入る前の画像符号化・確率モデルの橋渡し。
- 推奨前提：P06
- 限界・注意：画像圧縮の論文。時間方向の予測や長系列安定性を解いたとは扱わない。
- 根拠の確認範囲：要旨・書誌確認 — Google Research abstract / ICLR metadata
- 根拠：[原文](https://research.google/pubs/variational-image-compression-with-a-scale-hyperprior/) / [元資料](https://research.google/pubs/variational-image-compression-with-a-scale-hyperprior/)
- 状態：候補。利用者の既読状態は未確認。

## P08 — DVC: An End-To-End Deep Video Compression Framework

- 著者：Guo Lu; Wanli Ouyang; Dong Xu; Xiaoyun Zhang; Chunlei Cai; Zhiyong Gao
- 年・版：2019 / CVPR
- 識別子：https://openaccess.thecvf.com/content_CVPR_2019/html/Lu_DVC_An_End-To-End_Deep_Video_Compression_Framework_CVPR_2019_paper.html
- 論文：[公開ページ](https://openaccess.thecvf.com/content_CVPR_2019/html/Lu_DVC_An_End-To-End_Deep_Video_Compression_Framework_CVPR_2019_paper.html)
- 分類：学習型 / 転換点 / 共通導入
- 発見経路：前回答の多様な種
- 読む理由：動き・残差を学習器で符号化する構造を従来型と対応させる。
- 読む問い：**従来の予測構造を残しつつ、何を共同最適化したのか。**
- 他の候補との差：P10との対比に必要な残差符号化側の足場。
- 推奨前提：P01, P06, P07
- 限界・注意：主結果は特定のFFmpeg設定。別実装・presetへの優位性に拡張しない。
- 根拠の確認範囲：本文の構造・実験条件確認 — CVPR paper §3; §4.1–4.2
- 根拠：[原文](https://openaccess.thecvf.com/content_CVPR_2019/papers/Lu_DVC_An_End-To-End_Deep_Video_Compression_Framework_CVPR_2019_paper.pdf) / [元資料](https://openaccess.thecvf.com/content_CVPR_2019/papers/Lu_DVC_An_End-To-End_Deep_Video_Compression_Framework_CVPR_2019_paper.pdf)
- 状態：候補。利用者の既読状態は未確認。

## P09 — Scale-Space Flow for End-to-End Optimized Video Compression

- 著者：Eirikur Agustsson; David Minnen; Nick Johnston; Johannes Ballé; Sung Jin Hwang; George Toderici
- 年・版：2020 / CVPR
- 識別子：https://openaccess.thecvf.com/content_CVPR_2020/html/Agustsson_Scale-Space_Flow_for_End-to-End_Optimized_Video_Compression_CVPR_2020_paper.html
- 論文：[公開ページ](https://openaccess.thecvf.com/content_CVPR_2020/html/Agustsson_Scale-Space_Flow_for_End-to-End_Optimized_Video_Compression_CVPR_2020_paper.html)
- 分類：学習型 / 別設計 / 分岐候補
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：動き予測の不確実性と学習手順の単純化を見る。
- 読む問い：**隠れていた領域の出現や速い動きを、通常のワーピングからどう改善するか。**
- 他の候補との差：残差→条件付けだけでない設計軸をP08に追加する。
- 推奨前提：P08
- 限界・注意：要旨は低遅延・Bフレームなしと記載。詳しい実験設定と性能は未監査。
- 根拠の確認範囲：要旨・書誌確認 — CVF abstract
- 根拠：[原文](https://openaccess.thecvf.com/content_CVPR_2020/html/Agustsson_Scale-Space_Flow_for_End-to-End_Optimized_Video_Compression_CVPR_2020_paper.html) / [元資料](https://openaccess.thecvf.com/content_CVPR_2020/html/Agustsson_Scale-Space_Flow_for_End-to-End_Optimized_Video_Compression_CVPR_2020_paper.html)
- 状態：候補。利用者の既読状態は未確認。

## P10 — Deep Contextual Video Compression

- 著者：Jiahao Li; Bin Li; Yan Lu
- 年・版：2021 / NeurIPS
- 識別子：arXiv:2109.15047
- 論文：[公開ページ](https://proceedings.neurips.cc/paper_files/paper/2021/hash/96b250a90d3cf0868c83f8c965142d2a-Abstract.html)
- 分類：学習型 / 転換点 / 共通導入
- 発見経路：前回答の多様な種
- 読む理由：残差を固定的に作る設計から、特徴の条件付けへ比較する。
- 読む問い：**条件情報をencoder・decoder・entropy modelのどこでどう使うのか。**
- 他の候補との差：P08からの概念差を学ぶ。小さな性能差だけを選定理由にしない。
- 推奨前提：P07, P08
- 限界・注意：DVC原著と比較条件が異なる。著者らによる同条件での再評価と原著値を区別する。
- 根拠の確認範囲：本文の構造・実験条件確認 — NeurIPS paper §3–4.2
- 根拠：[原文](https://proceedings.neurips.cc/paper_files/paper/2021/file/96b250a90d3cf0868c83f8c965142d2a-Paper.pdf) / [元資料](https://proceedings.neurips.cc/paper_files/paper/2021/file/96b250a90d3cf0868c83f8c965142d2a-Paper.pdf)
- 状態：候補。利用者の既読状態は未確認。

## P11 — NeRV: Neural Representations for Videos

- 著者：Hao Chen; Bo He; Hanyu Wang; Yixuan Ren; Ser Nam Lim; Abhinav Shrivastava
- 年・版：2021 / NeurIPS
- 識別子：arXiv:2110.13903
- 論文：[公開ページ](https://neurips.cc/virtual/2021/poster/26386)
- 分類：動画別表現 / 別設計 / 分岐候補
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：動画をモデル重みとして表す別の符号化観を導入する。
- 読む問い：**符号化を動画ごとの最適化に置き換えると、どのコストが移動するか。**
- 他の候補との差：汎用モデルによる逐次符号化のP08/P10とは違う枝。
- 推奨前提：P06, P07
- 限界・注意：学習・適合時間と重みの符号量を要確認。実時間ストリーミングと同じ条件ではない。
- 根拠の確認範囲：要旨・書誌確認 — NeurIPS poster abstract
- 根拠：[原文](https://neurips.cc/virtual/2021/poster/26386) / [元資料](https://neurips.cc/virtual/2021/poster/26386)
- 状態：候補。利用者の既読状態は未確認。

## P12 — Towards Practical Real-Time Neural Video Compression

- 著者：Zhaoyang Jia; Bin Li; Jiahao Li; Wenxuan Xie; Linfeng Qi; Houqiang Li; Yan Lu
- 年・版：2025 / CVPR
- 識別子：arXiv:2502.20762
- 論文：[公開ページ](https://openaccess.thecvf.com/content/CVPR2025/html/Jia_Towards_Practical_Real-Time_Neural_Video_Compression_CVPR_2025_paper.html)
- 分類：学習型 / 実装制約 / 分岐候補
- 発見経路：前回答の多様な種
- 読む理由：圧縮率以外の実装コストとデバイス間整合性を読む。
- 読む問い：**演算量削減だけで速度が上がるか。整数化すると何を失い何を得るか。**
- 他の候補との差：P10系統の後続を、単なるRD改善でなく実用性の観点で選定する。
- 推奨前提：P10, P13, P14
- 限界・注意：A100・fp16の値を全GPUやint16に流用しない。コードの実行再現は未実施。
- 根拠の確認範囲：本文の構造・実験条件確認 — CVPR paper §5.1; Tables 2–3; Fig.5(c)
- 根拠：[原文](https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Towards_Practical_Real-Time_Neural_Video_Compression_CVPR_2025_paper.pdf) / [元資料](https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Towards_Practical_Real-Time_Neural_Video_Compression_CVPR_2025_paper.pdf)
- 状態：候補。利用者の既読状態は未確認。

## P13 — The Bjøntegaard Bible: Why your Way of Comparing Video Codecs May Be Wrong

- 著者：Christian Herglotz et al.
- 年・版：2023 / arXiv v2（受理記載あり）
- 識別子：arXiv:2304.12852
- 論文：[公開ページ](https://arxiv.org/html/2304.12852)
- 分類：評価 / 評価批判 / 共通導入
- 発見経路：前回答の多様な種
- 読む理由：BD値を読む際の補間・区間・測定誤差を学ぶ。
- 読む問い：**小さなBD差を本当の改善と判断するには何を確認するか。**
- 他の候補との差：手法提案のP08/P10/P12とは役割が異なり、比較の誤読を抑える。
- 推奨前提：P06
- 限界・注意：今回は要旨・導入を中心に確認。全数値実験の検算は未実施。
- 根拠の確認範囲：本文抜粋確認 — arXiv v2 Abstract / Introduction
- 根拠：[原文](https://arxiv.org/html/2304.12852) / [元資料](https://arxiv.org/html/2304.12852)
- 状態：候補。利用者の既読状態は未確認。

## P14 — The Practice of Averaging Rate-Distortion Curves over Testsets to Compare Learned Video Codecs Can Cause Misleading Conclusions

- 著者：M. Akin Yilmaz; Onur Keleş; A. Murat Tekalp
- 年・版：2024 / arXiv v2
- 識別子：arXiv:2409.08772
- 論文：[公開ページ](https://arxiv.org/html/2409.08772)
- 分類：評価 / 評価批判 / 共通導入
- 発見経路：前回答の多様な種
- 読む理由：データ集合の集約順序による結論の変化を理解する。
- 読む問い：**平均RD曲線とシーケンス別BD値の平均はなぜ違うのか。**
- 他の候補との差：P13の補間問題とは異なる集約の問題を補う。
- 推奨前提：P13
- 限界・注意：特定比較の例を全学習型研究の誤りと一般化しない。重み付けの目的も明示する。
- 根拠の確認範囲：本文抜粋確認 — arXiv v2 Abstract / §1–2 / references
- 根拠：[原文](https://arxiv.org/html/2409.08772) / [元資料](https://arxiv.org/html/2409.08772)
- 状態：候補。利用者の既読状態は未確認。

## P15 — Rethinking Lossy Compression: The Rate-Distortion-Perception Tradeoff

- 著者：Yochai Blau; Tomer Michaeli
- 年・版：2019 / ICML / PMLR 97
- 識別子：arXiv:1901.07821
- 論文：[公開ページ](https://proceedings.mlr.press/v97/blau19a.html)
- 分類：知覚・理論 / 原理 / 分岐候補
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：低歪みと知覚的自然さを別の目標として理解する。
- 読む問い：**忠実性・符号量・知覚品質を同時に改善できる範囲は何か。**
- 他の候補との差：PSNR中心の比較に対し、目的そのものを問い直す。
- 推奨前提：P06
- 限界・注意：画像・理論の基礎資料。動画の時間的一貫性や主観品質を直接保証するものではない。
- 根拠の確認範囲：要旨・書誌確認 — PMLR abstract / citation metadata
- 根拠：[原文](https://proceedings.mlr.press/v97/blau19a.html) / [元資料](https://proceedings.mlr.press/v97/blau19a.html)
- 状態：候補。利用者の既読状態は未確認。

## P16 — End-to-End Rate-Distortion Optimized Learned Hierarchical Bi-Directional Video Compression

- 著者：M. Akın Yılmaz; A. Murat Tekalp
- 年・版：2021 / arXiv v1（TIP受理記載；刊行版との差分未確認）
- 識別子：arXiv:2112.09529
- 論文：[公開ページ](https://arxiv.org/abs/2112.09529)
- 分類：学習型 / 別設計 / 分岐候補
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：低遅延だけに偏らず、階層的双方向予測を扱う。
- 読む問い：**未来フレームを使えると圧縮率・遅延・参照構造はどう変わるか。**
- 他の候補との差：P09/P10の逐次的条件と異なる時間構造を補う。
- 推奨前提：P08
- 限界・注意：要旨のx265/SVT-HEVC/HMへの主張を、低遅延方式との公平な順位に使わない。
- 根拠の確認範囲：要旨・書誌確認 — arXiv v1 abstract / acceptance comment
- 根拠：[原文](https://arxiv.org/abs/2112.09529) / [元資料](https://arxiv.org/abs/2112.09529)
- 状態：候補。利用者の既読状態は未確認。

## P17 — Deep Learning-Based Video Coding: A Review and A Case Study

- 著者：Dong Liu; Yue Li; Jianping Lin; Houqiang Li; Feng Wu
- 年・版：2020 / ACM Computing Surveys（確認資料はarXiv 2019 v1の要旨・書誌）
- 識別子：10.1145/3368405
- 論文：[公開ページ](https://arxiv.org/abs/1904.12462)
- 分類：学習・従来混合 / 全体像 / 分岐候補
- 発見経路：概念別キーワード検索・会議/出版社ページ確認
- 読む理由：学習型の新方式と、既存方式への学習ツール組込みを分ける。
- 読む問い：**規格や既存構造を維持しながら、どの部分を学習器にできるか。**
- 他の候補との差：エンドツーエンド論文だけに偏る候補集合を補正する。
- 推奨前提：P01
- 限界・注意：歴史的サーベイであり最新動向ではない。複数ツールを組み合わせた利得を一つの部品の効果にしない。
- 根拠の確認範囲：要旨・書誌確認 — arXiv abstract / journal reference
- 根拠：[原文](https://arxiv.org/abs/1904.12462) / [元資料](https://arxiv.org/abs/1904.12462)
- 状態：候補。利用者の既読状態は未確認。
