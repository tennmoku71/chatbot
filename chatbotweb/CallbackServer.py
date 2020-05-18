#!/usr/bin/env python

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from urllib import parse as urlparse

def start(address,port, callback, initfunc, bot_name, html=None):
    def handler(*args):
        CallbackServer(callback,initfunc,bot_name,html,*args)
    server = HTTPServer((address, int(port)), handler)
    print("server start")
    print("access : http://localhost:"+str(port))
    print("please press ctrl+c if you want to stop server")
    server.serve_forever()

class CallbackServer(BaseHTTPRequestHandler):

    def __init__(self, callback,initfunc, bot_name, html, *args):
        self.callback = callback
        self.initfunc = initfunc
        self.bot_name = bot_name
        self.html = html
        BaseHTTPRequestHandler.__init__(self, *args)

    def api_say(self):
        content_len  = int(self.headers.get("content-length"))
        contents = self.rfile.read(content_len).decode("utf-8")
        txt = dict(urlparse.parse_qsl(contents))["txt"]
        
        print("api sayが呼ばれました")
        self.send_response(200)
        self.end_headers()
        message = self.callback(txt)
        self.wfile.write(message.encode())
        return

    def show_form(self):
        self.send_response(200)
        self.end_headers()
        startup_utterance = self.initfunc()

        default_view = """
            <style>
                h1   { background-color: #ffe0e0; }
                div  { padding:10px; }
                span { border-radius: 10px; background-color: #ffe0e0; padding:8px; }
                .bot { text-align: left; }
                .usr { text-align: right; }
            </style>
            <h1>チャットボットと会話しよう</h1>
        """

        main_view = """
            <html><meta charset="utf-8"><body>
            <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
            <userdef>
            <div id="chat"><init_chat_html></div>
            <div class='usr'><input id="txt" size="40">
            <button onclick="say()">発言</button></div>
            <script>
            
            var url = ".";
            function htmlentities(str){
              return String(str).replace(/&/g, "&amp;")
                .replace(/"/g, "&quot;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;");
            }

            function say() {
              var txt = $('#txt').val();
              $.post(url, {"txt":htmlentities(txt)},
                function(res) {
                  
                  var html = "<div class='usr'><span>" + esc(txt) +
                    "</span>:あなた</div><div class='bot'><robot_name>:<span>" + 
                    esc(res) + "</span></div>";
                  $('#chat').html($('#chat').html()+html);
                  $('#txt').val('').focus();
                });
            }
            function esc(s) {
                return s.replace('&', '&amp;').replace('<','&lt;')
                        .replace('>', '&gt;');
            }
            </script></body></html>
            """

        message = None
        message = main_view.replace("<bot_name>",self.bot_name)
        
        if startup_utterance is not None:
            message = message.replace("<init_chat_html>","""<div class="bot">""" + self.bot_name + """:<span>""" + startup_utterance + """</span></div>""")
        else:
            message = message.replace("<init_chat_html>","")
        
        if self.html is not None:
            message = message.replace("<userdef>",self.html)
        else:
            message = message.replace("<userdef>",default_view)

        self.wfile.write(message.encode())
        return

    def do_GET(self):
        self.show_form()

    def do_POST(self):
        self.api_say()