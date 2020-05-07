#!/usr/bin/env python3
import cgi

# Windows環境でサーバーを起動したときの文字化けを防ぐための設定
# 標準出力の文字コードを utl-8 にする
import sys
import os
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sys.path.append(os.environ['PYTHON_CWD'])
import importlib

# chatbot_userdef.pyが存在するかどうかチェック
chatbot_userdef_spec = importlib.util.find_spec("chatbot_userdef")
if chatbot_userdef_spec is not None:
    import chatbot_userdef

# chatbot_userdef.htmlが存在するかどうかチェック
userdef_html_path = os.environ['PYTHON_CWD']+"/chatbot_userdef.html"
valid_userdef_html = os.path.exists(userdef_html_path)

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
    res = txt
    if chatbot_userdef_spec is not None:
        res = chatbot_userdef.get_answer(txt)
    print(res)

# フォームを画面に出力 --- (*4)
def show_form():
    print("Content-Type: text/html; charset=utf-8")
    print("")
    if valid_userdef_html:
        body = open("cgi-bin/base.html").read()
        body = body.replace("<userdef_html>", open(userdef_html_path).read())
        print(body)
    else:
        print(open("cgi-bin/default.html").read())

main()








