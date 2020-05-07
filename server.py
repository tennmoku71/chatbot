from http.server import HTTPServer, CGIHTTPRequestHandler
import os

class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]

def run(filepath, response_func=None, html_func=None):
    os.environ['PYTHON_CWD'] = filepath
    print("pid : "+str(os.getpid()))
    os.chdir(os.path.dirname(__file__))
    PORT = 8080
    httpd = HTTPServer(("", PORT), Handler)
    print("server start")
    print("access : http://localhost:8080/cgi-bin/chatbot.py")
    print("please press ctrl+c if you want to stop server")
    httpd.serve_forever()