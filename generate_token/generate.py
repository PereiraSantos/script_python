import hmac
import hashlib
import base64
import json
import subprocess

secret_key = '123456789'

header = json.dumps({
    'typ': 'JWT',
    'alg': 'HS256'
}).encode()

payload = json.dumps({
    'userId': '55395427-265a-4166-ac93-da6879edb57a',
    'exp': 1556841600,
}).encode()

b64_header = base64.urlsafe_b64encode(header).decode()
b64_payload = base64.urlsafe_b64encode(payload).decode()

signature = hmac.new(
    key=secret_key.encode(), 
    msg=f'{b64_header}.{b64_payload}'.encode(),
    digestmod=hashlib.sha256
).digest()

JWT = f'{b64_header}.{b64_payload}.{base64.urlsafe_b64encode(signature).decode()}'

proc = subprocess.run(["/home/user/script/generate_token/token.sh  %s"% (JWT)], shell=True)

#import jwt

#secret_key = '123'

#payload_data = {
#    "name": "Seu Nome",
#    "code": 1,
#    "mail": "exemplo@teste.com.br",
#    "password": "0",
#    "roles": "0, 1",
#}

#token = jwt.encode(
#    payload=payload_data,
#    key=secret_key
#)

#print(token)

