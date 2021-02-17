from flask import request
from flask_restful import Resource
from Security.enocdeDecode import Encryption, Decryption
from Resources.fetch import Fetch
from Security.hashing import Hashing
import requests


# Pay API
class Pay(Resource):

    def post(self):
        payload1 = {"data": {}}
        json_data = request.get_json()
        number = json_data["loan_number"]
        response = Fetch.post(number)
        if response["success"]:
            payload1["data"]["loan_number"] = number
            payload1["data"]["fetchID"] = response["details"]["fetchId"]
            payload1["data"]["amountPaid"] = 2000
            payload1["data"]["txnRefId"] = "12312asD"
            encoded = str(payload1["data"]).encode('utf-8')
            h = Hashing()
            val = h.hash(encoded, 'sha1')
            payload1["checksum"] = val

            abc = Encryption()
            payload = abc.encrypt(str(payload1), 'ase128ECB')
            print(payload)
            url = "https://4hfvpey3dk.execute-api.ap-south-1.amazonaws.com/v1/bill-apis/stage/modules/module/bbps" \
                  "/bills/receipt "
            headers = {
                'Content-Type': 'text/plain'
            }
            resp = requests.request("POST", url, headers=headers, data=payload)
            byte_text = resp.text
            cde = Decryption()
            response = cde.decrypt(byte_text, 'ase128ECB')
            if response["success"]:
                return response
            else:
                return {"message": "Data not found"}, 404
        else:
            return {"message": "Data not found"}, 404
