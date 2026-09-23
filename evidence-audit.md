# DCVC-RT 数値主張の証拠監査 — A100 fp16速度

## 判定

**125.2 / 112.8 fps（符号化 / 復号）は、条件付きの著者報告として引用できる。独立再現済み、全I/Oを含む製品end-to-end速度、又はint16の性能としては引用できない。** 対象は本文 Table 3(b) の1920×1080・A100・fp16の一組に限定した。本文§5.1の標準CPUは AMD EPYC 7V13で、異なるqpで平均latencyを計測すると記す。[1]

既存 `comparison-conditions.json` P12 / `comparison-memo.md` の未監査事項のうち、**速度の測定範囲**を、補足と公開実装まで追って具体化した。ただし「確認した公開実装の境界」と「論文実験当時の厳密な境界」を区別する。

## 本文 → 補足 → コード

### 1. 本文の主張

本文PDF p.8 Table 3(b)はfp16の125.2 / 112.8 fpsとint16の28.3 / 20.9 fpsを別行で示す。Table 3(a)のBD-rateもfp16 −21.0%、int16 −18.3%と異なる。本監査はfp16速度を対象とし、BD-rate再計算やint16速度再現は行っていない。[1]

### 2. 補足が解消する点

公式CVF landing pageのsuppリンクから取得した補足PDF pp.2–3 §2.3 / Fig.1は、1080pのnetwork inference約7.8 ms、entropy coding最大2.6 msと説明し、それらを部分的に並列化する。したがって「GPUネットワーク推論だけのfps」と読むのは不適切で、7.8+2.6 msの単純和からTable 3を検算するのも不適切である。[2]

補足は通常の符号化でreconstruction generationを省略すること、p.4 §3.3ではmodule latencyの和が全体latencyに等しくないことも明記する。単純なmodule合計や符号化＋復号の直列往復時間を、報告fpsと同一視しない。[2]

### 3. 公開コードで具体化した境界

検査版：Microsoft/DCVC **`cbdae87a5445114cdc7f48816da63ea80bdeac40`**、`DCVC-family/DCVC-RT/`。GitHub mainからSHAを解決してraw取得した公開版であり、論文実験snapshotとの同一性は未確認。現在のroot側の後続実装をDCVC-RTとして扱っていない。READMEは当該subtreeをCVPR2025の公式実装と記している。[3]

`test_video.py` の `run_one_point_with_stream` を追跡した結果：[4]

| 処理 | 確認した公開実装のfps用計時 |
|---|---|
| 入力読込、YUV420→444、device転送、fp16化 | 開始前（L74–91,173–176,261–263） |
| padding、compress、SPS/IP headerをメモリbufferへ書込 | 符号化に含む（L176–227） |
| bitstreamのdisk書込・disk読込 | 両計時区間の外（L237–247） |
| メモリbufferからheaderを読む、decompress、crop | 復号に含む（L263–291） |
| distortion算出、出力色変換、再構成file保存 | 復号終了後（L296–318） |
| CUDA処理完了待ち | 各開始直前と終了時に同期（L175,226,262,290） |
| 初期化・warmup | model loadは外。速度平均は先頭10frameを除外（L328–333） |

README L105–107も、`test_time` はI/Oと画質計算を含む総試験時間、fps用時間はこれらを除くと明記する。ログの `avg_frame_encoding_time` / `avg_frame_decoding_time` は**秒**の平均時間を保存し、console表示では1000倍してmsとしている。フィールド名に反してfps値そのものではない。[3][4][8]

`DMC.compress` L299–341は `encode_z`、`encode_y`、`flush`、`get_encoded_stream` を含み、実entropy bitstream生成を計時内で待つ。これは補足のparallel codingの説明と整合する。また通常P符号化はdecoderで参照featureを作って画像再構成を省くが、feature refreshの `prepare_feature_adaptor_i` L293–297には再構成があるため「符号化は常に再構成なし」とは言えない。[2][6]

### 4. 実行設定上の落とし穴

- READMEの例は `--verbose 0`。平均時間を出力・保存するには `--verbose 1` 以上かつ10frame超が必要。例の `--reset_interval 64` とparser既定値32も異なる。[3][4]
- `--force_intra_period -1` はconfigの値を強制的に−1へ書き換える指定ではない。上書きは正値のときだけ。有効な公開例configの53系列がすべて−1なので、この例ではsingle-intraになる。[4][5]
- single-intra時は速度平均から先頭I frameも除かれる一方、画質・bit集計のframe列は全frameのまま。**RDのall framesと速度のwarmup除外後を混同しない。**[4][8]
- READMEはCPU arithmetic codingとcustom CUDA kernelsにも言及する。A100というGPU名だけで同速度が保証されるとは言えない。[3]

## 実際に行った検証

保存したコードに対する13項目の静的検査を親側でも再実行し成功。モデルの実行・GPU測定・学習はしていない。速度値の逆数換算は単位換算にすぎず、数値再現ではない。

## 未確認と公開用表現

未確認なのは、論文のexact commit / checkpoint digest / ソフトウェア環境、速度測定の系列・qp一覧・反復回数・集約重み、raw timing logs、及びGPUでのfps独立再現。公開例configと現在のREADMEだけで、これらを確定しない。

推奨表現：

> DCVC-RT論文Table 3(b)は、NVIDIA A100（標準CPU: AMD EPYC 7V13）で1920×1080・fp16の平均符号化/復号速度125.2/112.8 fpsを報告する。補足と確認した公開DCVC-RT実装はentropy codingを含むcodec処理を裏付けるが、公開実装の速度計測は入力/出力I/Oや画質計算を除き、先頭10フレームも除外する。これは製品end-to-end速度やint16の性能ではなく、当該実装commitが論文実験snapshotと同一であること及び報告fpsの独立再現は未確認である。[1][2][4]

証拠URL、行/頁、解消事項、未確認事項、実行範囲は [evidence-audit.json](evidence-audit.json)にも保存した。取得した論文・補足・実装のコピーは公開しない。

## Sources

[1] https://openaccess.thecvf.com/content/CVPR2025/papers/Jia_Towards_Practical_Real-Time_Neural_Video_Compression_CVPR_2025_paper.pdf
[2] https://openaccess.thecvf.com/content/CVPR2025/supplemental/Jia_Towards_Practical_Real-Time_CVPR_2025_supplemental.pdf
[3] https://raw.githubusercontent.com/microsoft/DCVC/cbdae87a5445114cdc7f48816da63ea80bdeac40/DCVC-family/DCVC-RT/README.md
[4] https://raw.githubusercontent.com/microsoft/DCVC/cbdae87a5445114cdc7f48816da63ea80bdeac40/DCVC-family/DCVC-RT/test_video.py
[5] https://raw.githubusercontent.com/microsoft/DCVC/cbdae87a5445114cdc7f48816da63ea80bdeac40/DCVC-family/DCVC-RT/dataset_config_example_yuv420.json
[6] https://raw.githubusercontent.com/microsoft/DCVC/cbdae87a5445114cdc7f48816da63ea80bdeac40/DCVC-family/DCVC-RT/src/models/video_model.py
[8] https://raw.githubusercontent.com/microsoft/DCVC/cbdae87a5445114cdc7f48816da63ea80bdeac40/DCVC-family/DCVC-RT/src/utils/common.py
