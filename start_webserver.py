#runs a https server with $: python3 start_webserver.py

import http.server, ssl

server_address = ('0.0.0.0', 443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile='localhost.pem',
                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()

#Make sure you specify the right parameters for wrap_socket!

#The certificate can be generated using/ openssl req -new -x509 -keyout localhost.pem -out localhost.pem -days 365 -nodes

#get ip address

# ip route get 1.2.3.4 | awk "{print $1}"