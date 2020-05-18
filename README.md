# Chatbot Project

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
from chatbotweb import CallbackServer

def callback_method(text):
    if text == "Hello":
        return "Hello! Oni-chan!"
    else:
        return "Sorry, I don't know what you mean."

CallbackServer.start("0.0.0.0",8080, callback_method)
```

please access in this page
```
local access
http://localhost:8080

global access
http://[server global ip address]:8080
※ please open 8080 port of firewall
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

CallbackServer.start(8080, callback_method, html = myhtml)
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