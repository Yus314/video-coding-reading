# 更新・選別手順

## 正本と生成物

- **正本**：`papers.json`（書誌・注釈・根拠）、`relations.json`（引用/推奨順/対比）。
- **自動生成**：`annotated-bibliography.md`、`papers/Pxx.md`、`relations-view.md`。直接編集しない。
- **人が編集**：README、分野地図、読書順、系譜の考察、比較メモ、採否の考察。
- **補助データ**：`sources.json`、`search-log.json`、`screening.json`、`comparison-conditions.json`。
- **独立探索の正本**：`independent-review.json`。検索式とその探索回の採否を保持し、`independent-review.md`は手編集の解説。既存資料と同一なら`canonical_paper_id`で対応付け、P資料の現行書誌・確認状態は`papers.json`を使う。探索時の確認範囲は履歴として残す。
- **限定監査**：`evidence-audit.json`がP12監査の構造化記録、`evidence-audit.md`が手編集解説。`figure-checks.json`は実際に画像確認した図だけを列挙する。これらは論文全体の精読状態ではない。

P/S/F/ICは品質の順位ではない。新しい調査ごとに別の資料台帳を増やさず、通常の採否はscreening、独立探索の追記はindependent-reviewへ。F01/F02の既存案内はfollowup-reviewとscreeningに保持し、今回全面移行はしない。

個人の読書記録や非公開の取得キャッシュは生成物にも公開リポジトリにも混ぜない。論文本文を転載せずURLと節/図表の位置を残す。

## 追加・修正

1. DOI/arXiv/題名で同一成果を照合。版違いは二重計上せず、見た版を明記。
2. 通常の探索経路を `search-log.json`、具体的な採否を `screening.json` に記録。既存名簿を伏せる独立探索は `independent-review.json` に検索・探索時点・照合後の採否をまとめ、入口からリンクする。引用確認を後から行っても、初回発見を引用探索に書き換えない。
3. `papers.json` に問い・読む理由・代替候補との差・確認範囲を記す。本文を読んで根拠を補強できた場合にだけ `evidence_claims` に原文URLと節/図表を追加する。
4. `selection` に採否、重要性、代替、確信を分けて記す。`prerequisites` は推奨順、`required_background` は概念上の前提であり混同しない。
5. 必要な `relations.json` と手編集の地図/経路/比較メモを更新する。読む候補の追加が共通キューの増大を意味しないようにする。
6. 地図・経路・カード・比較メモに判断変更を反映する。未確認事項には「保留になる結論／それでも言えること／次に必要な証拠」を添え、用途と無関係な再現を読書の前提にしない。次を実行し、差分を確認して公開する。

```sh
python3 scripts/catalog.py build
python3 scripts/catalog.py check
python3 -m unittest discover -s tests -v
```

`check` は生成物を書き換えず、データ不整合と生成差分を検出する。詳しくは [開発手順](DEVELOPMENT.md)。テスト成功は注釈の内容が正しい証明ではなく、重要な主張は元論文で別途確認する。

## 採否と停止

被引用数・掲載先・BD値を総合スコアにしない。概念の役割、現在の集合への追加価値、代替、実験への確信を分ける。保留は質の否定ではない。

新着の自動採用や定期巡回はない。一巡ごとに「読書の順序や判断が何によって変わったか」を残し、未調査領域と未確認事項を明示する。全会議・引用網の探索完了を、単に追加候補が減ったことから主張しない。
