import http.server
import socketserver
import os

PORT = 5000
DIRECTORY = "docs"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Serving {DIRECTORY}/ at http://0.0.0.0:{PORT}")
    httpd.serve_forever()
