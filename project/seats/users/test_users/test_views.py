from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from ..views import register


class RegisterViewTest(TestCase):
    """This class tests the registration view."""

    def setUp(self):
        # Create request factory object to create test requests
        self.factory = RequestFactory()
        # Create request user with data
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_register_view_valid_post(self):
        """This method tests the view's behavior when a valid POST request is made to the view."""

        # Create POST request with valid data
        request = self.factory.post(reverse('register'), {
            'username': 'newuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'y`3jk^+PHNm5PSAA',
            'password2': 'y`3jk^+PHNm5PSAA'
        })

        # Set request user and session attribute
        request.user = self.user
        setattr(request, 'session', 'session')
        # Create FallbackStorage object and set message attribute
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        # Finally call view function on request
        response = register(request)

        # Check for successful redirect
        self.assertEqual(response.status_code, 302)
        # Check if user is redirected to login page
        self.assertEqual(response.url, '/login/')
        # Check if message object has a message
        self.assertEqual(len(messages), 1)
        # Check if correct message with username is prompted
        self.assertEqual(str(messages._queued_messages[0]), 'Account created for newuser')

    def test_register_view_invalid_post(self):
        """This method tests the view's behavior when an invalid POST request is made to the view."""

        # Create POST request with invalid data (username is missing)
        request = self.factory.post(reverse('register'), {
            'username': '',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'y`3jk^+PHNm5PSAA',
            'password2': 'y`3jk^+PHNm5PSAA'
        })

        # Set request user and session attribute
        request.user = self.user
        setattr(request, 'session', 'session')
        # Create FallbackStorage object and set message attribute
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        # Finally call view function on request
        response = register(request)

        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # Check if form validation error occurred
        self.assertContains(response, 'This field is required.')
        # Check if message object is empty
        self.assertEqual(len(messages), 0)

    def test_register_view_get_request(self):
        """This method tests the view's behavior when a GET request is made to the view."""

        # Create GET request using factory
        request = self.factory.get(reverse('register'))
        # Set request user and call register view
        request.user = self.user
        response = register(request)

        # Check for successful response
        self.assertEqual(response.status_code, 200)
        # Check if form was returned in response
        self.assertContains(response, '<form')
        # Check if response contains CSFR token
        self.assertContains(response, 'csrfmiddlewaretoken')
