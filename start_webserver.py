#Runs a Secured server with self signed certificate

import http.server, ssl


def run_server():
    server_address = ('0.0.0.0', 443)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                server_side=True,
                                certfile='localhost.pem',
                                ssl_version=ssl.PROTOCOL_TLS)
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()


#check https://curl.se/docs/sslcerts.html for further instructions
#https://michaelheap.com/curl-58-unable-to-set-private-key-file-server-key-type-pem/
#https://www.geeksforgeeks.org/ssl-certificate-verification-python-requests/

#run a simpe https local hose server with $: python3 -m http.server
#generate cacert
#openssl s_client -showcerts -servername samuel -connect 192.168.0.104:443 > cacert.pem

#Make sure you specify the right parameters for wrap_socket!

#The certificate can be generated using/ openssl req -new -x509 -keyout localhost.pem -out localhost.pem -days 365 -nodes

#get ip address

# ip route get 1.2.3.4 | awk "{print $1}"

#To generate public key pair from certificate, then copy it to godot .crt certificate file

#generate new private key pair
#openssl genrsa -des3 -out private.pem 2048

#generate public key pair
#openssl rsa -in private.pem -outform PEM -pubout -out public.pem

#make sure .crt file in godot engine contains public key for clients connectivity

#copy and paste .crt from web browser certificate
#generate new private key
#openssl genrsa -out private_key.pem 2048


#where private_key.pem == key file name
#2048 == bit size of the key

#To view the private key
#cat private_key.pem

# To generate public key from the private key
#openssl rsa -in private_key.openssl x509 -noout -modulus -in samuel.crt | openssl md5pem -outform PEM -pubout -out public_key.pem

#connect to server with terminal

#curl https://192.168.0.104/body.json  --cert localhost.pem  --key private.key --cacert cacert.pem

#check if public and private key match #if values are different, welp
#openssl rsa -noout -modulus -in private.key | openssl md5
#openssl x509 -noout -modulus -in samuel.crt | openssl md5
