from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.auth.models import User
from ..views import register


class RegisterViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_register_view_valid_post(self):
        request = self.factory.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpass123',
            'password2': 'newpass123',
        })
        request.user = self.user
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = register(request)
        self.assertEqual(response.status_code, 302)
        print(response.url)
        self.assertEqual(response.url, '/login/')
        self.assertEqual(len(messages), 1)
        #self.assertEqual(str(messages['cookie_name']), 'Account created for newuser')

    def test_register_view_invalid_post(self):
        request = self.factory.post(reverse('register'), {
            'username': '',
            'email': 'newuser@example.com',
            'password1': 'newpass123',
            'password2': 'newpass123',
        })
        request.user = self.user
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        response = register(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        self.assertEqual(len(messages), 0)

    def test_register_view_get_request(self):
        request = self.factory.get(reverse('register'))
        request.user = self.user
        response = register(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')
        self.assertContains(response, 'csrfmiddlewaretoken')
