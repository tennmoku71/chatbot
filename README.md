# Chatbot Project

## 概要
Python で作成した Chatbot です。
Web browser で web server を通してプログラムにアクセスします。
画面で文章を入力すると、ボットがなんらかの文章を返してきます。
ボットの文章作成にはマルコフ連鎖モデルを使用しています。
ユーザーが入力した文章はマルコフ連鎖用の辞書の形式で保存されていきます。

## 使い方
ディレクトリ cgi-bin から http サーバーを起動して、cgi-bin の下にある chatbot.py を Web browser で開きます。


## 前提とする環境

### Python バージョン

 - Python 3.7

### ライブラリ
 - Janome
 - cgi

## 出典
書籍：増補改訂 Pythonによるスクレイピング＆機械学習 [開発テクニック],  クジラ飛行机著