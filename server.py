# base httpserver example from...
# https://gist.github.com/bradmontgomery/2219997

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from example import show_files

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("got".encode("utf-8"))
        query_params = parse_qs(urlparse(self.path).query)
        print(query_params)
        show_files([query_params.filename], 10)

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("posted".encode("utf-8"))

    def do_HEAD(self):
        self._set_headers()


def run(server_class=HTTPServer, handler_class=S, port=1989):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print
    'Starting httpd...'
    httpd.serve_forever()


if __name__ == "__main__":
    run()