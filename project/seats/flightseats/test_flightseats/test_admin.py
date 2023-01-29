from django import forms
from django.test import RequestFactory, TestCase
from django.urls import reverse
from ..admin import SeatAdmin
import os


class SeatAdminTestCase(TestCase):
    def test_upload_txt(self):
        # create a fake request object with a POST request
        txt_data = '1\tA\tB\tC\tD\tE\tF\n' \
                   '2\tA\tB\tC\tD\tE\tF\n' \
                   '3\tA\tB\tC\tD\tE\tF'

        request = self._create_post_request(txt_data)

        # create an instance of the SeatAdmin class
        admin = SeatAdmin()

        # call the upload_txt function on the instance
        response = admin.upload_txt(request)

        # check that the response has the expected status code
        self.assertEqual(response.status_code, 200)

        # check that the file has been written with the correct data
        content = self._read_file_content()
        self.assertEqual(content, txt_data)

    def _create_post_request(self, txt_data):
        factory = RequestFactory()
        txt_file = SimpleUploadedFile("file.txt", txt_data.encode())
        return factory.post('/admin/flightseats/book/txt-upload/', {'txt_upload': txt_file})

    def _read_file_content(self):
        with open('flightseats/data/chartIn.txt', 'r') as f:
            return f.read()

    def tearDown(self):
        # clean up the file after the test
        if os.path.exists('flightseats/data/chartIn.txt'):
            os.remove('flightseats/data/chartIn.txt')

