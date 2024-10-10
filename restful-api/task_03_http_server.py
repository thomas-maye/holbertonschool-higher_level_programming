#!/usr/bin/python3
"""Develop a simple API using Python with the `http.server` module"""

import http.server
import json

PORT = 8000


class RequestHandler(http.server.BaseHTTPRequestHandler):
    """Handle HTTP requests"""

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!\n")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b'OK')

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found\n")


if __name__ == "__main__":
    # Create the server, binding to localhost on port 8000
    with http.server.HTTPServer(("", PORT), RequestHandler) as httpd:
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
