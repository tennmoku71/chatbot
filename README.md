# ChatbotWeb

## Overview
Web browser chat bot on python

### environmental

 - Python 3

## install

```
$ pip install chatbotweb
```

## how to use

```
#!/usr/bin/env python
# coding:utf-8

from chatbotweb.chat_server import ChatServer

class MyChatClass():

    BOT_NAME = "my bot"
    # override html file
    html = None

    # Run only once when the server starts
    def __init__(self):
        pass

class UserClass():

    # Run only once when accessing from an unknown IP address
    def __init__(self):
        pass

    # Run when the page is accessed
    # Return value : The first utterance spoken by the robot when accessing the site
    def init_function(self, query_params):
        return "hello"

    # Run when there is a user utterance
    # Return value : Robot utterance to user utterance
    def callback_method(self,text):
        return "response "+text

if __name__ == '__main__':

    address = "0.0.0.0"
    port = 8080
    chat_server = ChatServer(myChatClass, UserClass)
    chat_server.start(address, port)
```

please access in this page
```
local access
http://localhost:8080

global access
http://[server global ip address]:8080
※ please open 8080 port of firewall and set the port conversion of the router
```

## customize view

pleasse create chatbot_userdef.html
The tag described in chatbot_userdef.html is inserted inside the body element.
Use style or script tag if you want to add stylesheet or japascript 

```html:default.html
<!-- default -->

myhtml = """
<style>
    h1   { background-color: #ffe0e0; }
    div  { padding:10px; }
    span { border-radius: 10px; background-color: #ffe0e0; padding:8px; }
    .bot { text-align: left; }
    .usr { text-align: right; }
</style>
<h1>チャットボットと会話しよう</h1>
"""
CallbackServer.start(
    ip_address,
    port, 
    callback_method, 
    init_function, 
    bot_name, 
    html = myhtml
)
```

The default html looks like this
```html:base.html
<html>
  <meta charset="utf-8"><body>
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>

    <!-- insert your html here -->
    
    <div id="chat"></div>
    <div class='usr'><input id="txt" size="40">
    <button onclick="say()">発言</button></div>
    <script>
    var url = "./chatbot.py";
    function say() {
      var txt = $('#txt').val();
      $.get(url, {"m":"say","txt":txt},
        function(res) {
          var html = "<div class='usr'><span>" + esc(txt) +
            "</span>:you</div><div class='bot'>bot:<span>" + 
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
```


## reference
original https://github.com/HideKobayashi/chatbot