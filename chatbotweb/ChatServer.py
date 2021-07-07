from http.server import HTTPServer
from chatbotweb.Chathander import ChatRequestHandler

class ChatServer():

    def __init__(self,chat_obj):
        self.access_list = {}
        self.chat_obj = chat_obj

    def handler(self, *args):
        ip_address = args[1][0]
        user_obj = None
        if ip_address in self.access_list:
            user_obj = self.access_list[ip_address]
        else:
            user_obj = self.chat_obj.UserClass()
            self.access_list[ip_address] = user_obj

        return ChatRequestHandler(self.chat_obj,user_obj,*args)

    def start(self, address, port):
        server = HTTPServer((address, int(port)), self.handler)
        print("server start")
        print("access : http://localhost:"+str(port))
        print("please press ctrl+c if you want to stop server")
        server.serve_forever()