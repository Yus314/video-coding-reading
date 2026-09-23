# 比較条件メモ

P08・P10・P12は本文の実験節まで確認。改訂ではP07の符号化順序/評価の注意、P18の構造/制御節、P20の分類/実験条件も確認。全件精読とは区別する。**著者報告の抽出であり、独立追試はしていない。** 未確認を未記載と読み替えない。

## P08 DVC と P10 DCVCを数字だけで比べない

P08 §4.2はH.264/H.265をFFmpegの `very fast` modeで生成、GOPはUVG=12、HEVC=10と記載。詳細設定は補足参照。P10 §4はx264/x265を `veryslow`、constant QPに変更し、DVC/DVCProもDCVCと同じintra codecで再評価したと説明している。

したがって、原著の改善率の差をそのまま設計の効果にできない。比較するなら、同一の実験内で揃えた条件と、その変更を調べる。

根拠：[DVC本文](https://openaccess.thecvf.com/content_CVPR_2019/papers/Lu_DVC_An_End-To-End_Deep_Video_Compression_Framework_CVPR_2019_paper.pdf) §4.1–4.2 / [DCVC本文](https://proceedings.neurips.cc/paper_files/paper/2021/file/96b250a90d3cf0868c83f8c965142d2a-Paper.pdf) §4。

## P12 DCVC-RTの数値に条件を付ける

- 本文Table 2の従来型比較はHM-16.25、VTM-17.0、ECM-11.0。
- 全フレーム、intra-period=-1、low delay。訓練の品質階層のgroup of 8 picturesとは区別する。
- YUV420とRGBを評価。headersを含む実bit-streamsで再評価したと著者が明記。
- 速度計測のデフォルトはNVIDIA A100＋AMD EPYC 7V13、1920×1080。
- Table 3のA100ではfp16が125.2/112.8 fps、int16が28.3/20.9 fps（符号化/復号）。
- Table 3の平均BD-rateはfp16=-21.0%、int16=-18.3%（VTM基準）。fp16値はYUV420のTable 2と一致する。ここではTable 3の報告値として記録し、RGBへ同じ数値を適用しない。異なる精度の速度とBD値を混ぜない。

この値は著者の条件での報告であり、製品のend-to-end遅延、他のGPU、周期的なランダムアクセスへ一般化しない。補足のコマンド、色変換、集約実装、時間測定の境界は未監査。

根拠：[DCVC-RT本文](https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Towards_Practical_Real-Time_Neural_Video_Compression_CVPR_2025_paper.pdf) §5.1、Tables 2–3。

## 全候補に適用する抽出項目

- 比較実装・版・preset・config
- GOP、参照構造、intra period、lookahead、評価フレーム数
- データ集合・解像度・fps・内容・学習/テストの分離
- 色空間・変換・サブサンプリング・bit depth
- PSNR等の定義、成分/フレーム/シーケンスの集約
- 実bitstreamか推定符号量か。I-frame・header・副情報・適合重みを含むか
- BD計算法、重なり区間、測定点、補間、シーケンス別値と重み
- CPU/GPU、数値精度、符号化/復号、entropy coder等を含む計測範囲
- 長系列、scene cut、domain shift、失敗例

[comparison-conditions.json](comparison-conditions.json) は全候補の確認状態を保持する。未確認欄が残る間は総合性能ランキングにしない。


## P20のサーベイ実験をP12の結果と混ぜない

[P20](https://www.ijcai.org/proceedings/2025/1165.pdf) §5は先頭96フレームを使い、従来型HM-16.20/VTM-23.0をRandom Accessで評価する。LVCのintra-periodとGOPは32。P12はlow delay・intra-period=-1の条件であり、比較対象のモデル・実装版も異なる。

したがって「別サーベイではVTMとの差が残る」「P12ではVTMを上回る」という報告を、即座に矛盾や再現失敗と判定しない。同時に、サーベイの結論だけを引用して普遍的な学習型優位とも言わない。P20で報告されたMS-SSIMの改善を、主観評価の実証に置き換えない。

PDFから自動抽出されたグラフの数値表は原図との照合が未実施のため、この資料には採用していない。今回は本文に明記された条件と限定的な解釈だけを使う。

## P07：副情報と集約の読み方

[Hyperprior論文](https://arxiv.org/html/1802.01436v2) §3 / Fig.3–4は、hyperlatentを先に復号して画像latentの確率を得る順序と、副情報の符号量も損失に含むことを説明する。§4.2 / Fig.5ではPSNRの曲線が等lambda、MS-SSIMが補間した等rateで集約される。図の見た目だけで指標間の優劣をまとめない。

## 比較データの粒度

現段階の `comparison-conditions.json` は論文単位の監査メモ。異なる精度・GPU・色空間の結果を一行へ統合した性能ランキングではない。実験単位データベースへの全面移行やコード再現は今回の範囲外。
