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


