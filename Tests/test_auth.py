import unittest
import auth


class TestUserAuth( unittest.TestCase ):

    def test_register_user(self):
        username = 'asdf1'
        password = 'test4'
        name = 'test4'
        token = auth.user.register( username, password, name )
        self.assertTrue( isinstance( token, str ) )


    def test_login_user(self):
        username = 'asdf1'
        password = 'test4'
        auth_token = auth.user.login( username, password )
        self.assertTrue( isinstance( auth_token, str ) )


    def test_user_status(self):
        username = 'test1'
        password = 'test1'
        token = auth.user.login( username, password )
        details = auth.user.details( token )
        self.assertTrue( isinstance(details, dict) )
        self.assertTrue( details['token'] == token )


    def test_logout_user(self):
        username = 'test2'
        password = 'test2'
        token = auth.user.login( username, password )
        new_token = auth.user.status( token )
        self.assertTrue( auth.user.logout( new_token ) )
        status = auth.user.status( new_token )
        self.assertFalse( status )
