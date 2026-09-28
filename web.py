from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<!DOCTYPE html>
<html>
<head>
<title>Laptop Specifications</title>
</head>
<body>
<h1>Laptop Specifications</h1>

<p><strong>Name:</strong> DEEPAK.N</p>
<p><strong>Register Number:</strong> 26005420</p>

<h2>Laptop Details</h2>
<p><strong>Name:</strong> Acer (TL15-53M-G2)</p>
<p><strong>Processor:</strong> Intel(R) Core(TM) 5 210H (2.20 GHz)</p>
<p><strong>RAM:</strong> 16GB</p>
<p><strong>Storage:</strong> 477 GB</p>
<p><strong>OS:</strong> Windows 11 Home Single Language</p>

</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running...")
httpd.serve_forever()