from django.test import TestCase
import tempfile


class TestReadFile(TestCase):

    def test_file_reading(self):
        with open('flightseats/data/chartIn.txt') as f:
            content = f.readlines()
        self.assertEqual(content, '12')

