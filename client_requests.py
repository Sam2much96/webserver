import requests
import ssl

requests.packages.urllib3.disable_warnings()



ssl.match_hostname = lambda cert, hostname: True

#response = requests.get('https://192.168.0.104/body.json',verify=False) #works


response = requests.get('https://192.168.0.104/body.json',verify='/home/samuel/webserver/samuel.pem')

#set verification to false to not use ssl verification

#ssl.match_hostname = lambda cert, hostname: hostname == cert['samuel'][0][1]

print (response.text)
#debug server connection in terminal

#curl https://192.168.0.104/body.json  --cert samuel.pem  --key samuel.pem --cacert cacert.pem

#debug server certificates
#check if public and private key match #if values are different, welp
#openssl rsa -noout -modulus -in private.key | openssl md5
#openssl x509 -noout -modulus -in samuel.crt | openssl md5


