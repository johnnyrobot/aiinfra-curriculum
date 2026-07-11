import http.server, socketserver, os
os.chdir(os.path.join(os.path.dirname(__file__), "..", "site"))
PORT = 8099
with socketserver.TCPServer(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler) as h:
    print(f"serving site/ at http://127.0.0.1:{PORT}")
    h.serve_forever()
