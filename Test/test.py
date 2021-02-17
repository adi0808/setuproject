import flask_unittest
from Security.enocdeDecode import Encryption, Decryption
from app import app as flask_app


# Test cases for Encryption and Decryption
class TestApi(flask_unittest.ClientTestCase):
    app = flask_app

    def test_encryption(self, client):
        expected_out = 'lcPYqqEsiNDe9UwxIF4FqQ9id7eoFQaVJVCH4iIiCtCQlkRRozMcetNlvKpGLJPgKnutBG' \
             '/gSEw/QlGTpZxzzFlVsnyF0z72CEmbvjmp+T6DSpL3ncRCNVc3UzgK/MGL'
        req = "{'data': {'loan_number': 'BAS123JKE'}, 'checksum': '23141339587d3a7eba4e0fb8b77795b587cfbcd7'}"
        a = Encryption()
        actual_output = a.encrypt(str(req), 'ase128ECB')
        self.assertEqual(actual_output.decode('utf-8'), expected_out)

    def test_decryption(self, client):
        expected_output = {'data': {'loan_number': 'BAS123JKE'}, 'checksum': '23141339587d3a7eba4e0fb8b77795b587cfbcd7'}
        req = 'lcPYqqEsiNDe9UwxIF4FqQ9id7eoFQaVJVCH4iIiCtCQlkRRozMcetNlvKpGLJPgKnutBG' \
              '/gSEw/QlGTpZxzzFlVsnyF0z72CEmbvjmp+T6DSpL3ncRCNVc3UzgK/MGL'
        b = Decryption()
        actual_output = b.decrypt(req, 'ase128ECB')
        self.assertEqual(actual_output.get('loan_number'), expected_output.get('loan_number'))
        self.assertEqual(actual_output.get('checksum'), expected_output.get('checksum'))