#!/usr/bin/env python
# coding:utf-8

from chatbotweb import CallbackServer

def init_function():
	return

def callback_method(text):
    return "response "+text

if __name__ == '__main__':
    CallbackServer.start("0.0.0.0",3000, callback_method, init_function)