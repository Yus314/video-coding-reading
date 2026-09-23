# 映像符号化：文献地図と目的別の読書案内

**selection-and-maintenance-2** — 20論文＋3補助資料。初期集合を別系統の資料から見直し、学習上の役割と確認範囲を付けたコレクションです。最新の網羅調査・普遍的な必読順位・codec性能ランキングではありません。

## 最初に開く

1. [目的別の読む順序](reading-queue.md) — AVC/RDO＋短い評価チェックから、規格・学習型・実装・知覚へ分岐
2. [分野地図](field-map.md) — 問い・技術・不足している領域
3. [注釈付き候補一覧](annotated-bibliography.md) — JSONから生成した全論文の問い・選定理由・根拠
4. [選定の再評価](selection-review.md) — 追加した理由、残した理由、保留した理由
5. [比較条件メモ](comparison-memo.md) — preset/GOP/精度/ハードウェアなどの誤読を防ぐ
6. [系譜の解釈](lineage.md) / [関係の生成一覧](relations-view.md) — 実引用と推奨学習順を区別

## この改訂の変化

- 学習型中心だった共通キューを短縮し、目的別経路に分離。
- P18（学習状態）、P19（従来型レート制御・要旨確認の仮候補）、P20（2025サーベイ）を追加。新着を無条件に必読化しない。
- 中心論文の説明を本文の節・図表に結び付け、P07の符号化順序と評価集約の確認を補強。
- 一覧・個別カード・関係一覧を正本JSONから生成し、二重編集を解消。

## データと更新

`papers.json` / `relations.json` が生成ビューの正本です。`sources.json` は原文URL、`screening.json` は今回の採否、`search-log.json` は探索経路、`comparison-conditions.json` は比較条件と未確認事項を保持します。

```sh
python3 scripts/catalog.py build
python3 scripts/catalog.py check
python3 -m unittest discover -s tests -v
```

Python標準ライブラリのみ。外部サービス・データベース・常駐処理は不要です。[更新手順](workflow.md) / [開発手順](DEVELOPMENT.md)を参照。

## 補助資料（論文候補と別カウント）

- **S01** [JVET/VVC](https://vvc.hhi.fraunhofer.de/)：CTC・VTMの入口。研究に対応する文書版を確認する。
- **S02** [Wohlinのsnowballing方法論](https://www.wohlin.eu/ease14.pdf)：探索方法の参考。映像符号化で最適性を実証したものではない。
- **S03** [Yang/Mandt/Theis: An Introduction to Neural Data Compression](https://arxiv.org/pdf/2202.06533v3.pdf)：情報理論・学習型損失の補助教材。確認箇所は目次・§3.7等で、全章精読ではない。

## 確認範囲と公開範囲

注釈・読書順はAIアシスタントによる編集案であり、利用者の既読・理解・意見を推定していません。要旨/本文箇所/実験条件の確認を分け、未確認を未記載と扱いません。P19は本文取得できず索引収録の著者要旨まで。全件精読・コード再現・2026年の網羅的検索は未実施です。

書誌、独自注釈・比較メモ、原文リンクのみを公開します。第三者のPDF・本文キャッシュや個人の読書記録は含みません。論文の権利は各権利者に帰属します。リポジトリ全体への再利用ライセンスは現時点では指定していません。
