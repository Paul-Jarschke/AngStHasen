from django.test import TestCase
from ..forms import UserRegisterForm


class UserRegisterFormTest(TestCase):
    """This class checks the validity of the register form, given valid and invalid data."""
    def test_form_validation_valid_data(self):
        """Test registration form using valid data."""
        # Create data
        form_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'y`3jk^+PHNm5PSAA',
            'password2': 'y`3jk^+PHNm5PSAA'
        }
        # Create form using form_data
        form = UserRegisterForm(form_data)
        # Check that from is valid
        self.assertTrue(form.is_valid())

    def test_form_validation_invalid_username(self):
        """Test registration form using invalid data (missing username)."""
        # Create data
        form_data = {
            'username': '',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'y`3jk^+PHNm5PSAA',
            'password2': 'y`3jk^+PHNm5PSAA'
        }
        # Create form using form_data
        form = UserRegisterForm(form_data)
        # Check that from is invalid
        self.assertFalse(form.is_valid())

    def test_form_validation_invalid_first_name(self):
        """Test registration form using invalid data (missing first name)."""
        # Create data
        form_data = {
            'username': 'testuser',
            'first_name': '',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'y`3jk^+PHNm5PSAA',
            'password2': 'y`3jk^+PHNm5PSAA'
        }
        # Create form using form_data
        form = UserRegisterForm(form_data)
        # Check that from is invalid
        self.assertFalse(form.is_valid())

    def test_form_validation_invalid_last_name(self):
        """Test registration form using invalid data (missing last name)."""
        # Create data
        form_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': '',
            'email': 'testuser@example.com',
            'password1': 'y`3jk^+PHNm5PSAA',
            'password2': 'y`3jk^+PHNm5PSAA'
        }
        # Create form using form_data
        form = UserRegisterForm(form_data)
        # Check that from is invalid
        self.assertFalse(form.is_valid())

    def test_form_validation_invalid_email(self):
        """Test registration form using invalid data (invalid email)."""
        # Create data
        form_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'iamnotanemail',
            'password1': 'y`3jk^+PHNm5PSAA',
            'password2': 'y`3jk^+PHNm5PSAA'
        }
        # Create form using form_data
        form = UserRegisterForm(form_data)
        # Check that from is invalid
        self.assertFalse(form.is_valid())

    def test_form_validation_non_matching_password(self):
        """Test registration form using invalid data (passwords don't match)."""
        # Create data
        form_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'y`3jk^+PHNm5PSAA',
            'password2': 'y`3jk^+PHNm5PSA1'     # password2 differs slightly
        }
        # Create form using form_data
        form = UserRegisterForm(form_data)
        # Check that from is invalid
        self.assertFalse(form.is_valid())
