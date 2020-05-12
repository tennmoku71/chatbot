#!/usr/bin/env python
# coding:utf-8

from chatbotweb import CallbackServer

def callback_method(text):
    return "response "+text

if __name__ == '__main__':
    CallbackServer.start(8080, callback_method)