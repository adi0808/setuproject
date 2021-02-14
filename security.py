import base64
import hashlib
import json
from random import Random

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = "assignmentToSetu".encode('utf-8')
BLOCK_SIZE = 16


def encrypt(info):
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
    raw = pad(info)
    cipher = AES.new(key, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(raw.encode('utf-8')))

def decrypt(info):
    enc = base64.b64decode(info)
    cipher = AES.new(key, AES.MODE_ECB)
    response = unpad(cipher.decrypt(enc), block_size=BLOCK_SIZE)
    return response


if __name__ == "__main__":
    # encrypted_req = "35O+Ss56p7jQCOxuUZQX2qCnuI321cVFJbmnKypTufGx+tRp2L6EQVFu9b8NATu0zOjXj3MyJpf4yDKnc638N3/Il87icK7GVI2qZBiO/0gH7BNLgH8nP17jNkaBuAi3"
    # print("encrypted request : ", encrypted_req)
    # decrypted_resp = decrypt(encrypted_req)
    # print("decrypted response : ", type(decrypted_resp))
    # x = json.loads(decrypted_resp)
    # print(type(x))
    # print(x["status"])
    # print(x["success"])
    # print(x["details"]["receiptId"])


    # print("========================")
    # decrypted_req = "{\"data\": {\"loan_number\":\"BAS123JKE\"},\"checksum\":\"4406f3578082e33d1b16c0a7da74d2eb921eab48\"}"
    # print("decrypted request : ", decrypted_req)
    # encrypted_response = encrypt(decrypted_req)
    # print("encrypted response: ", encrypted_response)
    # # print("encrypted request : ", encrypted_req)
    # decrypted_resp = decrypt(encrypted_response)
    # print("decrypted response : ", decrypted_resp)




    data = {"data": {"loan_number": "BAS123JKE"}}
    encoded = json.dumps(data).encode('utf-8')
    result = hashlib.sha1(encoded)
    checksum = str(result.hexdigest())
    print(type(checksum))
    print(data["data"])
    load = {"data": data["data"], "checksum": checksum}
    payload = encrypt(str(load))
    print(payload)
    print("-------------------------------------")
    decrypted_resp = decrypt(payload)
    de = decrypted_resp.decode('utf-8')
    x = json.loads(de)
    print(type(x))


