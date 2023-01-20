from django.test import TestCase
from ..models import Flight


class TestModels(TestCase):

    def setUp(self):
        pass

    def test_model_str(self):
        airline = Flight.object.create(airline='Test Airline')
    pass
