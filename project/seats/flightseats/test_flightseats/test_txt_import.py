from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, TestCase
from ..admin import SeatAdmin
from ..models import Book


class SeatAdminTestCase(TestCase):
    """This class tests the upload of a new .txt file for the seat layout."""
    def test_upload_txt(self):
        # Create an instance of the SeatAdmin
        seat_admin = SeatAdmin(admin_site='/admin/', model=Book)

        # Create a RequestFactory instance
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

        # Create a file-like object to simulate a file upload
        txt_file = SimpleUploadedFile("file.txt", file_input_bytes)

        # Create a POST request
        request = factory.post("/txt-upload/", {"txt_upload": txt_file})
        request.method = "POST"

        # Call the `upload_txt` function
        seat_admin.upload_txt(request)

        # Check if the file has been written correctly
        with open("flightseats/data/chartIn.txt", "r") as f:
            content = f.read()
            f.close()

        # Check for equal content
        self.assertEqual(content, file_input_bytes.decode('utf-8') + "\n")
