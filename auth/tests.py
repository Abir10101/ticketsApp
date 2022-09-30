import unittest
import secrets
from auth.utils import *


class TestJwtToken( unittest.TestCase ):

    def test_encode_auth_token(self):
        user_id = 1
        secret = secrets.token_urlsafe(10)
        token = encode_auth_token( user_id, secret )
        self.assertTrue( isinstance( token, str ) )


    def test_decode_auth_token(self):
        user_id = 3
        secret = secrets.token_urlsafe(10)
        token = encode_auth_token( user_id, secret )
        self.assertTrue( isinstance( token, str ) )
        decoded = decode_auth_token(token)
        self.assertTrue( isinstance( decoded, dict ))
