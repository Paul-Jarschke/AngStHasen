from django.test import TestCase
from ..forms import UserRegisterForm


class UserRegisterFormTest(TestCase):
    """This class checks the validity of the register form, given valid and invalid data."""
    def test_form_validation_valid_data(self):
        # Test form with valid data
        form_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'y`3jk^+PHNm5PSAA',
            'password2': 'y`3jk^+PHNm5PSAA'
        }
        form = UserRegisterForm(form_data)
        # Check that from is valid
        self.assertTrue(form.is_valid())

    def test_form_validation_invalid_data(self):
        # Test form with invalid data
        form_data = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password1': 'password123',
            'password2': 'password456'
        }
        form = UserRegisterForm(form_data)
        # Check that form is invalid
        self.assertFalse(form.is_valid())
