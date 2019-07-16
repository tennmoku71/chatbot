#!/usr/bin/env python3
import cgi
from botengine import make_reply


# Windows環境でサーバーを起動したときの文字化けを防ぐための設定
# 標準出力の文字コードを utf-8 にする
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# フォームからの入力を得る --- (*1)
form = cgi.FieldStorage()

# メイン処理 --- フォームの値で分岐する --- (*2)
def main():
    m = form.getvalue("m", default="")
    if   m == "" : show_form()
    elif m == "say" : api_say()

# ユーザーの入力に対して返答を返す処理 --- (*3)
def api_say():
    print("Content-Type: text/plain; charset=utf-8")
    print("")
    txt = form.getvalue("txt", default="")
    if txt == "": return
    res = make_reply(txt)
    print(res)

# フォームを画面に出力 --- (*4)
def show_form():
    print("Content-Type: text/html; charset=utf-8")
    print("")
    with open("cgi-bin/form.html", "r") as f:
        content = f.readlines()  
    for line in content:
        print(line, end="")

main()








