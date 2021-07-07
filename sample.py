#!/usr/bin/env python
# coding:utf-8

from chatbotweb.chatserver import ChatServer

class MyChatClass():

    BOT_NAME = "my bot"
    html = None

    def __init__(self):
        pass

class UserClass():

	def __init__(self, chat_obj):
		self.chat_obj = chat_obj

    def init_function(self, query_params):
        return "hello"

    def callback_method(self,text):
        return "response " + text

if __name__ == '__main__':

    address = "0.0.0.0"
    port = 3000
    chat_server = ChatServer(myChatClass,UserClass)
    chat_server.start(address, port)