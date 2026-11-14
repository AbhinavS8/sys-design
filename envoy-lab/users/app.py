import os, socket
from http.server import BaseHTTPRequestHandler, HTTPServer

NAME = os.getenv("NAME", "service")

class H(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == "/health":
			self.send_response(200); self.end_headers();
			self.wfile.write(b"ok"); return

		if self.path.startswith("/fail"):
			self.send_response(503); self.end_headers();
			self.wfile.write(b"boom"); return

		body = f"{NAME} | host={socket.gethostname()} | path={self.path}\n"
		self.send_response(200); self.end_headers();
		self.wfile.write(body.encode())

HTTPServer(("0.0.0.0", 8000), H).serve_forever()
