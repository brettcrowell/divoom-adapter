# base httpserver example from...
# https://gist.github.com/bradmontgomery/2219997

from sys import argv
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from example_commands import ExampleCommands

class S(BaseHTTPRequestHandler):

    def _set_divoom(self):
        if not hasattr(self, "commands"):
            self.commands = ExampleCommands(argv[1])

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("got".encode("utf-8"))
        query_params = parse_qs(urlparse(self.path).query)
        self._set_divoom()

        action = query_params["action"][0]
        value = query_params["value"][0]

        with self.commands as commands:
            if (action == "show_file"):
                commands.show_file(value)
            elif (action == "draw_text"):
                commands.draw_text(value)

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