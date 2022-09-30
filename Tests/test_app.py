import unittest
from app.utils import add_ticket


class TestAppFunc( unittest.TestCase ):

    def test_add_ticket(self):
        user_id = '1'
        ticket_number = '1232'
        ticket_description = 'asdf'
        ticket_status = 'asdf'
        try:
            ticket_id = add_ticket(user_id, ticket_number, ticket_description, ticket_status)
        except Exception as err:
            self.assertEqual( f"{err}", "Invalid Status" )
        ticket_status = 'done'
        ticket_id = add_ticket(user_id, ticket_number, ticket_description, ticket_status)
        self.assertTrue( isinstance( ticket_id, int ) )
