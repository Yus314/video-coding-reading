# 開発・生成手順

## 必要環境

Python 3 の標準ライブラリだけを使用する。追加依存関係はない。

## コマンド

リポジトリルートで次を実行する。

```console
python3 scripts/catalog.py check
python3 scripts/catalog.py build
python3 -m unittest discover -s tests -v
```

テスト用など、別のルートを対象にする場合は `--root PATH` を指定できる。

```console
python3 scripts/catalog.py build --root /tmp/catalog-fixture
python3 scripts/catalog.py check --root /tmp/catalog-fixture
```

`build` は最初に `papers.json` と `relations.json` を検証し、成功した場合だけ生成物を書く。既知の論文に対応しない `papers/P*.md` がある場合は、ファイルを黙って削除せず停止する。`check` はデータを検証した後、期待する生成バイト列と実ファイルを読み取り専用で比較する。

## ファイルの所有区分

正規のメタデータは `papers.json`、論文間の関係は `relations.json` に置く。次のファイルだけが生成物であり、先頭に自動生成ヘッダーが付く。

- `annotated-bibliography.md`
- `papers/Pxx.md`（実際の ID ごとに一件。件数や ID は固定しない）
- `relations-view.md`

`field-map.md`、`reading-queue.md`、`lineage.md`、`comparison-memo.md` は手動管理であり、生成処理は変更しない。私的な読書メモ、キャッシュ、全文、認証情報は生成ビューや正規メタデータに入れず、リポジトリ外で管理する。

`prerequisites` と `recommended_before` は証明上の依存関係ではなく、推奨学習順である。既存の部分的な根拠確認を完全読了として記録せず、`status` と根拠の確認範囲をそのまま明示する。このツールは順位付けを行わない。

## 生成表示の重複整理

カードと一覧は読む問いを先頭に置く。分類と重複する役割行、および表示文字列が完全一致する重要性・補完性の再掲だけを省略する。意味が似ているという推測で異なる文章を消さない。正本の項目は保持する。重複省略・異なる説明の保持・問いの位置を回帰テストで確認する。

## 読書案内の整合検査

`nnpf-reading.md`は手編集の会合準備ガイドで、主候補論文の自動生成カードとは別に管理する。本文の出典番号は同ページ末尾の出典一覧に対応する。対象会合、確認基準日、規格・WD・TuC・個別提案の区別と確認範囲を保持し、第三者の原文や抽出全文は収録しない。

`nnpf-aq0155-walkthrough.md`は原文対照の読解例、`nnpf-aq0155-evidence.json`はその版・位置・確認方法の記録。出典番号とリンクの検査は構造整合に限り、削除後の構文の妥当性、採否、実装適合性の証明ではない。

`tests/test_reading_integrity.py` は手編集を含むMarkdownの相対リンク先、P/ICの参照先、独立候補の既存論文への対応、図・監査記録の参照整合を確認する。リンクのfragment、外部URLの常時到達性、本文未読を読み終えたとする誤記、引用の意味、学習効果は保証しない。新たな書誌を増やす前に既存IDへの対応を確認し、重要な意味変更は原文で別途点検する。
