from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Server 2</h1></body></html>")

def run():
    server_address = ('', 8001)
    httpd = HTTPServer(server_address, MyServer)
    print('Server running at localhost:8001...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
