from django.test import TestCase


class TestUrls(TestCase):

    def setUp(self):
        print('Starting setUp')

    def test_home_page(self):
        response = self.client.get('/')
        # Status code 200 represents successful response
        self.assertEqual(response.status_code, 200)
