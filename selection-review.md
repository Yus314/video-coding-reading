# 選定の再評価

## この改訂で変えた判断

- **共通導入の中立化**：初版の共通キューは後半が学習型だった。P01/P06＋評価チェックを共通にし、P07/P08/P10は学習型経路へ移動。P13/P14の精読を全員の入口条件にしない。
- **別設計P18を採用**：RippelらのLearned Video Compressionは、学習状態・共同表現・空間レート制御を扱う。DVC/DCVCだけの一本線を避けるために選定。S03 §3.7もこの設計を紹介し、P10の参考文献[16]にも収録される。被引用数順位や唯一の原点という意味ではない。
- **従来型rate control P19を仮採用**：RDOとは違う、目標rateへ合わせる枝の入口。本文未取得のため、式や効果の確信は引き上げない。
- **P20を地図に追加、P17は維持**：2025年のE2E/システムの地図と、2019年プレプリントで確認したhybrid toolsの地図は役割が異なる。新しさだけで置き換えない。
- **S03を補助教材に追加**：情報理論・学習型損失の前提を補うモノグラフ。全章読了を求めず、確認した§3.7等と案内だけの章を区別する。

## 別視点をどう得たか

- [Yang/Mandt/Theisのモノグラフ](https://arxiv.org/pdf/2202.06533v3.pdf)の目次・§3.7・参考文献[153]を確認。学習型の基本概念と別の設計選択を確認した。
- [IJCAI 2025サーベイ](https://www.ijcai.org/proceedings/2025/1165.pdf)の§2–5を確認。単方向/双方向、rate control、整数化、モバイル実装を分離した。
- P20からMobileNVC、Neural Rate Controlへ後方探索し、公式/著者公開要旨を確認して保留した。

別著者の資料は独立した視点を増やすが、著者の研究上の関心・自分の方式への言及を排除した中立性の証明ではない。サーベイの性能主張は原実験の条件で解釈する。

## 採用しなかった候補

- **MobileNVC** — [arXiv v3](https://arxiv.org/abs/2310.01258v3)。モバイル用のblock motion、整数化、並列復号pipelineはP12との差になる。ただし本文・端末・計測範囲は未監査。実用経路を深める際の候補に留める。
- **Neural Rate Control for Learned Video Compression** — [ICLR 2024要旨](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8c1d92835eb4e601f396c97ec60439fe-Abstract-Conference.html)。rate allocationとrate implementationを分ける設計は有望な比較題材。P19との公平な性能比較を要旨だけで行わず、学習型rate controlを重点化した時に読む。

保留は低品質という判定ではない。本文確認の予算と、今回の読書経路への追加価値を踏まえた編集判断。

## 今回の証拠の限界

候補採否の機械可読記録は [screening.json](screening.json)。検索経路は [search-log.json](search-log.json)。全候補・全会議・引用網の網羅や探索の飽和は主張しない。最新2026年の代表性、分野全体の必読合意、コード再現は未検証。
