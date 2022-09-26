import unittest
from app.functions import encode_auth_token, decode_auth_token, add_user


class TestUser( unittest.TestCase ):

    def test_encode_auth_token(self):
        user_id = 1
        token = encode_auth_token( user_id )
        self.assertTrue( isinstance( token, str ) )


    def test_decode_auth_token(self):
        user_id = 3
        token = encode_auth_token( user_id )
        self.assertTrue( isinstance( token, str ) )
        self.assertTrue( decode_auth_token(token) == 3 )


    def test_add_user(self):
        username = 'test1'
        password = 'test1'
        name = 'test1'
        token = add_user( username, password, name )
        self.assertTrue( isinstance( token, str ) )



if __name__ == '__main__':
    unittest.main()
