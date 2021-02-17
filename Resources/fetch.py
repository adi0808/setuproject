from flask import request
from flask_restful import Resource
from Security.enocdeDecode import Encryption, Decryption
from Security.hashing import Hashing
import requests


# Fetch API
class Fetch(Resource):

    def post(self):
        json_data = request.get_json()
        number = json_data["loan_number"]
        payload1 = {"data": {"loan_number": number}}
        encoded = str(payload1["data"]).encode('utf-8')
        h = Hashing()
        val = h.hash(encoded, 'sha1')
        payload1["checksum"] = val
        abc = Encryption()
        payload = abc.encrypt(str(payload1), 'ase128ECB')
        url = "https://4hfvpey3dk.execute-api.ap-south-1.amazonaws.com/v1/bill-apis/stage/modules/module/bbps/bills" \
              "/fetch "
        headers = {
            'Content-Type': 'text/plain'
        }
        resp = requests.request("POST", url, headers=headers, data=payload)
        byte_text = resp.text
        cde = Decryption()
        response = cde.decrypt(byte_text, 'ase128ECB')
        if response["status"] == 200:
            return response
        else:
            return response


