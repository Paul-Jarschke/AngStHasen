from django.test import RequestFactory, TestCase
from django.urls import reverse
from ..admin import SeatAdmin
import os


class SeatAdminTestCase(TestCase):
    def test_upload_txt(self):
        # create a fake request object with a POST request
        factory = RequestFactory()
        txt_file = open('file.txt', 'w')
        txt_file.write('1    A    B    C    D    E    F\n'
                       '2    A    B    C    D    E    F\n'
                       '3    A    B    C    D    E    F')

        request = factory.post('/admin/flightseats/book/txt-upload/', {'txt_upload': txt_file})
        txt_file.close()

        # create an instance of the SeatAdmin class
        admin = SeatAdmin()

        # call the upload_txt function on the instance
        response = admin.upload_txt(request)

        # check that the response has the expected status code
        self.assertEqual(response.status_code, 200)

        # check that the file has been written with the correct data
        with open('flightseats/data/chartIn.txt', 'r') as f:
            content = f.read()
            self.assertEqual(content, '1    A    B    C    D    E    F\n'
                                      '2    A    B    C    D    E    F\n'
                                      '3    A    B    C    D    E    F')

        # clean up the file after the test
        os.remove('flightseats/data/chartIn.txt')