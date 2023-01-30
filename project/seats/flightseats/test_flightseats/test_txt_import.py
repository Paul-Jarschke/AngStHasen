from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, TestCase
from ..admin import SeatAdmin
from ..models import Book


class SeatAdminTestCase(TestCase):
    def test_upload_txt(self):
        # create an instance of the SeatAdmin
        seat_admin = SeatAdmin(admin_site='/admin/', model=Book)

        # create a RequestFactory instance
        factory = RequestFactory()

        file_input_bytes = b'1\tA\tB\tC\tD\tE\tF\n'\
                           b'2\tA\tB\tC\tD\tE\tF\n'\
                           b'3\tA\tB\tC\tD\tE\tF\n'\
                           b'4\tA\tB\tC\tD\tE\tF\n'\
                           b'5\tA\tB\tC\tD\tE\tF\n'\
                           b'6\tA\tB\tC\tD\tE\tF\n'\
                           b'7\tA\tB\tC\tD\tE\tF\n'\
                           b'8\tA\tB\tC\tD\tE\tF\n'\
                           b'9\tA\tB\tC\tD\tE\tF\n'\
                           b'10\tA\tB\tC\tD\tE\tF\n'\
                           b'11\tA\tB\tC\tD\tE\tF\n'\
                           b'12\tA\tB\tC\tD\tE\tF\n'

        # create a file-like object to simulate a file upload
        txt_file = SimpleUploadedFile("file.txt", file_input_bytes)

        # create a POST request
        request = factory.post("/txt-upload/", {"txt_upload": txt_file})
        request.method = "POST"

        # call the `upload_txt` function
        seat_admin.upload_txt(request)

        # check if the file has been written correctly
        with open("flightseats/data/chartIn.txt", "r") as f:
            content = f.read()
            f.close()

        # Check for equal content
        self.assertEqual(content, file_input_bytes.decode('utf-8') + "\n")
