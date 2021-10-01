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
    # Return value : Robot utterance to user utterance and whether to continue the dialogue
    def callback_method(self,text):
        return "response "+text, True

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

## reference
original https://github.com/HideKobayashi/chatbot