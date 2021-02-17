import base64
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = "assignmentToSetu".encode('utf-8')


# Encryption class and methods
class Encryption:
    def encrypt(self, info, format):
        encryption_type = get_encryption_format(format)
        return encryption_type(info)


def get_encryption_format(format):
    if format == 'ase128ECB':
        return _aes128ecb_encryption
    else:
        raise ValueError(format)


def _aes128ecb_encryption(info):
    block_size = 16
    cipher = AES.new(key, AES.MODE_ECB)
    padded = lambda s: s + (block_size - len(s) % 16) * chr(16 - len(s) % 16)
    info = padded(info)
    response = base64.b64encode(cipher.encrypt(info.encode('utf-8')))
    return response


# Decryption class and methods
class Decryption:
    def decrypt(self, info, format):
        decryption_type = get_decryption_format(format)
        return decryption_type(info)


def get_decryption_format(format):
    if format == 'ase128ECB':
        return _aes128ecb_decryption
    else:
        raise ValueError(format)


def _aes128ecb_decryption(info):
    block_size = 16
    enc = base64.b64decode(info)
    cipher = AES.new(key, AES.MODE_ECB)
    response = unpad(cipher.decrypt(enc), block_size=block_size)
    new_response = (response.decode('utf-8')).replace("\'", "\"")
    resp = json.loads(new_response)
    return resp



#
#
#     url = "https://4hfvpey3dk.execute-api.ap-south-1.amazonaws.com/v1/bill-apis/stage/modules/module/bbps/bills/fetch"
#
#     payload = "VAsuXX7Pjs6G5PDQwteWsUkM0B5Zv94UFKqFe5tZLdRZYaBKFMU8e7r1YGpy3TgC7yu0R8FLa9+Iy3H05xQ21Fgg1bZNMwpe7osoNu19BqKN5R4CHDeWjTT7nn0lcQQwm+LsHNW2+FXa5wcpn5aD1w=="
#     headers = {
#         'Content-Type': 'text/plain'
#     }
#
#     resp = requests.request("POST", url, headers=headers, data=payload)
#     byte_text = resp.text
#     cde = Decryption()
#     response = cde.decrypt(byte_text, 'ase128ECB')
#     if (response["success"]):
#         print(response)
#     else:
#         print(response["error"])
#
# #
#     # # Decryption
#     # print("Decryption ------------------")
#     # cde = Decryption()
#     # c = cde.decrypt(b, 'ase128ECB')
#     # print(c)
#
#     # x = json.loads(c)
#     # print(x)
#     # # print(x["details"]["fetchId"])
#
#
#
#
#
#
