# 映像符号化の文献案内

論文名を集めるだけでなく、**何のために、どこを読み、どの条件まで信じられるか**を整理した公開資料です。最新の網羅調査や性能ランキングではありません。

## まず一つだけ読むなら

分野全体の勉強を始める前に、目的に合う作業を一つ選べます。所要時間は未測定です。

- **圧縮器の基本構造**：[HEVCの案内](conventional-reading.md)からP02 **II-A / Fig.1**。原画像と再構成参照の違いを追う。両者がなぜ必要か説明できたら、他の規格の全ツール一覧は後回し。
- **学習型の副情報**：[Hyperprior原文](https://arxiv.org/pdf/1802.01436v2) **§3 / Fig.4**。`zの復号 → 確率パラメータ → yの復号`を追う。[六つの問い](reading-lab.md)は分からない箇所だけ使う。
- **別論文へ読み方を応用**：[Scale-Space Flow原文](https://openaccess.thecvf.com/content_CVPR_2020/papers/Agustsson_Scale-Space_Flow_for_End-to-End_Optimized_Video_Compression_CVPR_2020_paper.pdf) **Fig.2 / §3.2**。DVC等で動き・残差の基本を理解済みなら、動きlatentからResidual Decoderへの接続も追い、[案内末尾のP09例](reading-lab.md)と照合する。性能表は今は不要。
- **速度の報告を評価**：[DCVC-RT監査](evidence-audit.md)の「判定」と「公開コードで具体化した境界」。含む処理・除く処理・未確認を分ける。モデルを実行しなくても測定範囲の理解は進められる。

## 目的から始める

### 仕組みを理解したい

- **従来型の構造・規格の違い** → [HEVC・VVC・AV1の読む箇所](conventional-reading.md)
- **新しい方式の図を読み解く** → [送信・生成・保持を六つの問いで追う](reading-lab.md)
- まだ分野を選んでいない → [全体の地図](field-map.md) / [目的別の読み順](reading-queue.md)

既に分かる部分は飛ばせます。指定節を読むことと、全論文を通読することは区別しています。

### 性能や設計の主張を判断したい

[比較条件と判断できる範囲](comparison-memo.md)から始めてください。具体例は[DCVC-RTの速度主張を補足・コードまで追う監査](evidence-audit.md)。実装・preset・時間構造・精度・ハードウェアが違う数値を、無条件の優劣にまとめません。

長系列や条件付き符号化の限界が気になる場合だけ、[目的限定の後続研究](followup-review.md)へ進みます。

### なぜこれらを選んだか確かめたい

[選定と見直しの記録](selection-review.md)を参照してください。[全候補の注釈](annotated-bibliography.md)は資料を探す索引であり、全件の読了要求ではありません。

## 資料と確認範囲

登録候補20論文、補助資料S01–S03に加え、目的限定の論文参照F01/F02と保留候補があります。分類を分けても資料が増える事実は変わりません。既存の採否は [screening.json](screening.json)、探索経路は [search-log.json](search-log.json)。追加の[独立探索8候補と採否](independent-review.md)には既存論文2件も含まれ、書籍・規格・教材・実装文書を論文数へ混ぜていません。検索式と確認範囲は [independent-review.json](independent-review.json)に記録します。

- **S01** [JVET/VVC](https://vvc.hhi.fraunhofer.de/)：規格・CTC・VTMの入口。
- **S02** [Wohlinのsnowballing方法論](https://www.wohlin.eu/ease14.pdf)：探索方法の参考。
- **S03** [An Introduction to Neural Data Compression](https://arxiv.org/pdf/2202.06533v3.pdf)：必要な前提を補う教材。

各カードに、要旨・指定本文・実験条件の確認範囲を記載しています。中心図の視覚確認は [figure-checks.json](figure-checks.json)。全件精読、全図点検、全実験再現、読者の学習効果測定はしていません。注釈と読書順は編集案であり、利用者の既読や意見を推定していません。

## 更新・再利用

正本はJSON、一覧とカードは自動生成、読書案内の文章は手編集です。[更新手順](workflow.md) / [開発手順](DEVELOPMENT.md) / [引用・推奨関係](relations-view.md)。

```sh
python3 scripts/catalog.py build
python3 scripts/catalog.py check
python3 -m unittest discover -s tests -v
```

Python標準ライブラリのみ。第三者の論文本文・PDF・原図キャッシュや個人の読書記録は公開しません。論文の権利は各権利者に帰属し、このリポジトリ全体の再利用ライセンスは未指定です。
