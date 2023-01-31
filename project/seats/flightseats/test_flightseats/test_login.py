from django.test import Client, TestCase
from django.contrib.auth.models import User


class LoginTestCase(TestCase):
    """This class tests the functionality of the login page."""
    def test_login_valid(self):
        """Test the validation of the login process with valid credentials."""
        # Create Client
        self.client = Client()
        # Create valid user credentials
        self.username = 'PaulDerGroße'
        self.password = 'lecker!paulanerspezi'
        # Create user object with given credentials
        User.objects.create_user(username=self.username, password=self.password)

        # Post login data in login page
        response = self.client.post('/login/', {'username': self.username, 'password': self.password})
        # Check for successful redirect (successful login should redirect to flight page)
        self.assertEqual(response.status_code, 302)
        # Check that user is logged in by checking session
        self.assertIn('_auth_user_id', self.client.session)
