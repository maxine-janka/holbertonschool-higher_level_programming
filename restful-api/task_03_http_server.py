#!/usr/bin/python3
"""A simple API using the http.server module"""

import http.server
import json


class RequestHandler(http.server.BaseHTTPRequestHandler):
    """A basic web server to handle different HTTP requests,
      inherits from BaseHTTPRequestHandle"""

    def do_GET(self):
        """Handles GET requests"""
        if self.path == "/":
            self.send_response(200)  # Send response status
            self.send_header("Content-type", "text/plain")  # Send headers
            self.end_headers()  # Define end of headers
            # Send response body
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            dataset = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            json_data = json.dumps(dataset)
            self.wfile.write(json_data.encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            infodata = {
                "version": "1.0",
                "description": "A simple API"
            }
            json_infodata = json.dumps(infodata)
            self.wfile.write(json_infodata.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))


port = 8000


def run_server(port):
    """Run the local server"""
    # Automatic close and clean up
    with http.server.HTTPServer(("", port), RequestHandler) as localserver:
        print("Local server running on port: {}".format(port))
        localserver.serve_forever()


# Prevent autorun: Only run server when file executed directly
if __name__ == "__main__":
    run_server(port)
