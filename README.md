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
$ import os
$ from chatbotweb import server
$ userdef_path = os.path.dirname(os.path.abspath(__file__))
$ server.run(userdef_path)
```

please access in this page
```
http://localhost:8080/cgi-bin/chatbot.py
```

## customize chatbot engine

pleasse create chatbot_userdef.py and get_answer function

```python:chatbot_userdef.py
# chatbot_userdef.py
def get_answer(text):
    if text == "Hello":
        return "Hello! Oni-chan!"
    else:
        return "Sorry, I don't know what you mean."
```

first argument is user input string data and you have to return any string data(chatbot utterance)

## customize view

pleasse create chatbot_userdef.html
The tag described in chatbot_userdef.html is inserted inside the body element.
Use style or script tag if you want to add stylesheet or japascript 

```html:chatbot_userdef.html
<!-- chatbot_userdef.html -->

<style>
    h1   { background-color: #ffe0e0; }
    div  { padding:10px; }
    span { border-radius: 10px; background-color: #ffe0e0; padding:8px; }
    .bot { text-align: left; }
    .usr { text-align: right; }
</style>
<h1>チャットボットと会話しよう</h1>
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