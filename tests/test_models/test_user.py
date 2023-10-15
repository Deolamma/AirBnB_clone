"""This is the unittest file for user.py file"""
from datetime import datetime
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Run tests for the User class"""

    def setUp(self):
        """Creates a simple object or instance of User"""
        self.my_model = User()

    def test_types(self):
        """Test the attribute type"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.email, str)
        self.assertIsInstance(self.my_model.password, str)
        self.assertIsInstance(self.my_model.first_name, str)
        self.assertIsInstance(self.my_model.last_name, str)

    def test_str_rep(self):
        """Test the string representation"""
        output = "[User] ({}) {}".format(
            self.my_model.id,
            self.my_model.__dict__
        )
        self.assertEqual(str(self.my_model), output)
