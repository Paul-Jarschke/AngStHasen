from django.test import TestCase
from django.urls import reverse, resolve
from ..views import register


class TestUrls(TestCase):
    def test_register_url_resolve(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)

