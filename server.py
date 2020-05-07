from http.server import HTTPServer, CGIHTTPRequestHandler

class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]

def run():
    PORT = 8080
    httpd = HTTPServer(("", PORT), Handler)
    httpd.serve_forever()