# base httpserver example from...
# https://gist.github.com/bradmontgomery/2219997

from sys import argv
from http.server import BaseHTTPRequestHandler, HTTPServer
from example_commands import ExampleCommands
import json

class S(BaseHTTPRequestHandler):

    def _set_divoom(self):
        if not hasattr(self, "commands"):
            self.commands = ExampleCommands(argv[1])

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("got".encode("utf-8"))

    def do_POST(self):
        self._set_headers()
        self.wfile.write("posted".encode("utf-8"))
        self._set_divoom()

        length = int(self.headers["content-length"])
        payload = self.rfile.read(length)
        data = json.loads(payload.decode("utf-8"))

        action = data["action"]
        value = data["value"]

        with self.commands as commands:
            if action == "show_file":
                commands.show_file(value)
            elif action == "draw_text":
                commands.draw_text(value)
            elif action == "show_pixel_array":
                commands.show_pixel_array(value)

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
