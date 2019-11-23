# Chatbot プロジェクトの前提とする環境の作り方

## 概要
Chatbot プロジェクトのソースコードをダウンロードしてみたけど、「前提とする環境」とか書かれてもよくわからない人のために、もう少し詳しく説明します。

## 1. Python のインストール

下記からダウンロードしてインストールしてください。

https://www.anaconda.com/

または

https://docs.conda.io/en/latest/miniconda.html

または

https://www.python.org/

## 2. テキストエディタ のインストール
すでにお好みのエディタがインストールされている場合はそれでもよいですが、特にない場合は、Visual studio Code がおすすめです。下記からダウンロードしてインストールしてください。

https://code.visualstudio.com/

## 3. （オプション）Git for Windows のインストール

下記のサイトからダウンロードしてインストールしてください。
Windows の方のみです。

https://gitforwindows.org/

Mac の場合は最初から OS に含まれています。

## 4. チャットボットソースコードのダウンロード

上記のインストールが済んだら、やることは下記です。

デスクトップに pyworks という名前のフォルダを作成してください。

チャットボット のソースコードを

https://github.com/HideKobayashi/chatbot

からダウンロードして、pyworks の下に展開してください。
展開すると　chatbot-master というフォルダができると思います。


## 5. チャットボットの動作確認

続いて、Anaconda prompt （あるいはコマンドプロンプト）を開いて、下記ような手順を行うと、チャットボットを起動することができます。
(上記のGitHub のページにも書いてます）

### 5-1. 形態素解析ライブラリ Janome をインストール

```sh
$ pip install janome
```

### 5-2. chatbot-master フォルダを ディレクトリごと chatbot へコピーする。

Windows の場合

```sh
cd Desktop\pyworks
xcopy /I /S chatbot-master chatbot
```

Mac の場合
```sh
cd Desktop/pyworks
cp -a chatbot-master chatbot
```

### 5-3. chatbot フォルダで http サーバーを立ち上げる
```sh
$ cd chatbot
$ python -m http.server --cgi 8080
```
（Mac の場合は python の代わりに python3 としてください。）

### 5-4. チャットボットを起動する

Web ブラウザで

http://localhost:8080/cgi-bin/chatbot.py  

にアクセスする。


### 5-5. チャットボットの使い方

文字を入力したあと、発言ボタンを押してください。
（エンターキーで発言できるようにするのも改良したい点です。）

## 開発のヒント

ソースコードは visual studio code で開けば見ることができます。

ソフトウエアを改良するアイデアとしては、次のようなものが考えられます。（難易度順）

1. 画面の見た目（色や文字やフォントなど）を変更する。
2. 会話の内容を好きなジャンル（カレー、アニメ、旅行など）のものが多くなるようにする。
3. 「今何時？」と送ると現在の時刻を答えるようにする。
4. 発言内容に応じて会話の内容ジャンルを切り替えるようにする。
5. 「東京の天気を教えて」と送ると今日の天気予報を表示する。