#!/usr/bin/env python3
"""Server suite-landing — ThreadingHTTPServer (patrón BMOPS)."""
import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

os.chdir("/root/suite-landing")
PORT = 8943

class H(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    def log_message(self, *a):
        pass

if __name__ == "__main__":
    print(f"suite-landing en :{PORT}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), H).serve_forever()
