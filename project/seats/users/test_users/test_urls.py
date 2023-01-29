from django.test import TestCase
from django.urls import reverse, resolve
from ..views import register


class TestUrls(TestCase):
    """
        Test class for testing URLs in Django.
    """
    def test_register_url_resolve(self):
        # Get URL string corresponding to name
        url = reverse('register')
        # Check that corresponding view function is called
        self.assertEqual(resolve(url).func, register)

