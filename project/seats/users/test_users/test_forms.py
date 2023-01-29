from django.test import TestCase
from ..forms import UserRegisterForm


class UserRegisterFormTest(TestCase):

    def test_register_form(self):
        # Create test user data
        data = {
            'email': 'paul@test.de',
            'username': 'Name',
            'password1': 'test12345',
            'password2': 'test12345'
        }
        # insert data to
        form = UserRegisterForm(data)
        self.assertTrue(form.is_valid())
