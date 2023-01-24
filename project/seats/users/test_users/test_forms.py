from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from ..forms import UserRegisterForm


class UserRegisterFormTest(TestCase):

    def test_register_form(self):
        data = {
            'email': 'paul@test.de',
            'username': 'Name',
            'password1': 'test12345',
            'password2': 'test12345'
        }
        form = UserRegisterForm(data)
        self.assertTrue(form.is_valid())
