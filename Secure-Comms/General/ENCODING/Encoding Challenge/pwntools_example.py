from pwn import * # pip install pwntools
import json
import base64
import codecs
from binascii import unhexlify

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def array_to_string(s):
    output = ""
    return(output.join(s))

for i in range(0,101):
    received = json_recv()
    if "flag" in received:
        print("\n Required FLAG: {}".format(received["flag"]))
        break
 
    print("Iteration carried : {}".format(i))
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    encoding_type = received["type"]

    string_to_decode = received["encoded"]
    if encoding_type == "base64":
        decoded_value =  base64.b64decode(string_to_decode).decode('utf-8')
    elif encoding_type == "hex":
        decoded_value =  (unhexlify(string_to_decode)).decode('utf-8')
    elif encoding_type == "rot13":
        decoded_value = codecs.decode(string_to_decode, 'rot13')
    elif encoding_type == "bigint":
        decoded_value = unhexlify(string_to_decode.replace("0x","")).decode('utf-8')
    elif encoding_type == "utf-8":
        decoded_value = array_to_string([chr(b) for b in string_to_decode])

    to_send = {
        "decoded": decoded_value 
    }
    json_send(to_send)