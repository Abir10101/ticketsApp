import unittest
import secrets
from auth import *


class TestUser( unittest.TestCase ):

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


    def test_register_user(self):
        username = 'test3'
        password = 'test3'
        name = 'test1'
        token = user.register( username, password, name )
        self.assertTrue( isinstance( token, str ) )


    def test_login_user(self):
        username = 'test1'
        password = 'test1'
        auth_token = user.login( username, password )
        self.assertTrue( isinstance( auth_token, str ) )


    def test_user_status(self):
        username = 'test1'
        password = 'test1'
        token = user.login( username, password )
        new_token = user.status( token )
        self.assertTrue( isinstance(token, str) )
        self.assertTrue( new_token == token )


    def test_logout_user(self):
        username = 'test2'
        password = 'test2'
        token = user.login( username, password )
        new_token = user.status( token )
        self.assertTrue( user.logout( new_token ) )
        status = user.status( new_token )
        self.assertFalse( status )



if __name__ == '__main__':
    unittest.main()
