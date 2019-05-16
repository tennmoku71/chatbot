# Chatbot Project

## 概要
Python で作成した Chatbot です。
Web browser で web server を通してプログラムにアクセスします。
画面で文章を入力すると、ボットがなんらかの文章を返してきます。
ボットの文章作成にはマルコフ連鎖モデルを使用しています。
ユーザーが入力した文章はマルコフ連鎖用の辞書の形式で保存されていきます。

## 使い方
ディレクトリ cgi-bin から http サーバーを起動してください。

```
$ python3 -m http.server --cgi 8080
```

Web browser を開いたら、下記の URL を入力することによって cgi-bin の下にある chatbot.py を開いてください。
```
ttp://localhost:8080/cgi-bin/chatbot.py
```


## 前提とする環境

### Python バージョン

 - Python 3.7

### ライブラリ
 - Janome
 - cgi

## 出典
書籍：増補改訂 Pythonによるスクレイピング＆機械学習 [開発テクニック],  クジラ飛行机著

クジラ飛行机こと kujirahand さん、ありがとうございます。あなたが本に書かれていたソフトウエアをリミックスして発展させていきたいと思います。