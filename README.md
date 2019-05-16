# Chatbot Project

## 概要
Python で作成した Chatbot です。
Web browser で web server を通してプログラムにアクセスします。
画面で文章を入力すると、ボットがなんらかの文章を返してきます。
ボットの文章作成にはマルコフ連鎖モデルを使用しています。
ユーザーが入力した文章はマルコフ連鎖用の辞書の形式で保存されていきます。

## 使い方
Mac の場合はターミナル、Windows の場合はコマンドプロンプトか bash on windows を開いてください。ソースコードを chatbot というディレクトリ以下に展開したものとして、以下説明します。ディレクトリ chatbot に移って http サーバーを起動してください。

```
$ python3 -m http.server --cgi 8080
```

Web browser を開いたら、下記の URL を入力することによって cgi-bin の下にある chatbot.py を開いてください。
```
http://localhost:8080/cgi-bin/chatbot.py
```
こうすると、ページの一番上に「チャットボットと会話しよう」という文字がピンク色の帯の中に表示されます。これがチャットの画面です。

## 前提とする環境

### Python バージョン

 - Python 3.7

### ライブラリ
 - Janome
 - cgi

cgi は標準ライブラリなので、改めてインストールしなくても入っているはずです。
 Python を Anaconda でインストールした場合は、なるべく conda でインストールを試みてください。具体的には `conda search janome` でライブラリパッケージを検索します。 
見つかったら、`conda install janome` でインストールします。
パッケージが conda でみつからない場合には、`pip install janome` でインストールします。


## 出典
書籍：増補改訂 Pythonによるスクレイピング＆機械学習 [開発テクニック],  クジラ飛行机著

クジラ飛行机こと kujirahand さんに感謝します。
