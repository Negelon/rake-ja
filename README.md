# rake-ja
Rapid Automatic Keyword Extraction algorithm for Japanese.

This module builds on [rake-nltk](https://github.com/csurfer/rake-nltk).


## Setup

```sh
$ git clone https://github.com/kanjirz50/rake-ja.git
$ cd rake-ja
$ python setup.py install
```

## Quick start

```python
>>> from rake_ja import JapaneseRake, GinzaTokenizer
>>> tok = GinzaTokenizer()
>>> ja_rake = JapaneseRake()
>>> # MeCab を使用する際は以下 : 
>>> from rake_ja import Tokenizer
>>> tok = Tokenizer()
>>> ja_rake.set_tokenizer(tok)
>>> # Wikipediaの記事から引用
>>> text = """「人工知能」という名前は1956年にダートマス会議でジョン・マッカーシーにより命名された。
現在では、記号処理を用いた知能の記述を主体とする情報処理や研究でのアプローチという意味あいでも使われている。
日常語としての「人工知能」という呼び名は非常に曖昧なものになっており、多少気の利いた家庭用電気機械器具の制御システムやゲームソフトの思考ルーチンなどがこう呼ばれることもある。"""
>>> tokens = tok.tokenize(text)
>>> ja_rake.extract_keywords_from_text(tokens)
>>> ja_rake.get_ranked_phrases_with_scores()
[(4.0, '記号 処理')
(4.0, '日常 語')
(4.0, '思考 ルーチン')
(4.0, '制御 システム')
(1.0, '非常')
(1.0, '記述')
(1.0, '研究')
(1.0, '知能')
(1.0, '現在')
(1.0, '気')
(1.0, '曖昧')
(1.0, '意味あい')
(1.0, '情報処理')
(1.0, '年')
(1.0, '家庭用電気機械器具')
(1.0, '呼び名')
(1.0, '名前')
(1.0, '会議')
(1.0, '人工知能')
(1.0, '主体')
(1.0, 'ゲームソフト')
(1.0, 'アプローチ')
(1.0, 'もの')
(1.0, 'こと')]
```
