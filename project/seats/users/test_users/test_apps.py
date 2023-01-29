from django.contrib.auth import get_user_model
from django.apps import apps
from django.test import TestCase


class TestUsersConfig(TestCase):
    """
        This class is used to test the configuration of the `users` app.

        It tests the default auto field setting, checks that the correct number
        of users have been created, and tests the attributes of several users.
    """
    def setUp(self):
        # Set up User model
        self.UserModel = get_user_model()

    def test_default_auto_field(self):
        # Get config for users app
        user_config = apps.get_app_config('users')
        # Check default auto field setting
        self.assertEqual(user_config.default_auto_field, 'django.db.models.BigAutoField')

    def test_users_created(self):
        # Check that 4 users have been created
        self.assertEqual(self.UserModel.objects.count(), 4)
        # Check that 1 user is staff
        self.assertEqual(self.UserModel.objects.filter(is_staff=True).count(), 1)
        # Check that 1 user has is superuser
        self.assertEqual(self.UserModel.objects.filter(is_superuser=True).count(), 1)

    def test_user_attributes(self):
        # Get the admin user
        admin_user = self.UserModel.objects.get(username='LeonHase')
        # Check that the admin user's email
        self.assertEqual(admin_user.email, 'leon@pythonexperts.com')
        # Check that the admin user's first name
        self.assertEqual(admin_user.first_name, 'Leon')
        # Check that the admin user's last name is 'Löppert'
        self.assertEqual(admin_user.last_name, 'Löppert')

        # Get the first normal user
        normal_user_1 = self.UserModel.objects.get(username='Janniboy_xD')
        # Check email
        self.assertEqual(normal_user_1.email, 'janlovesplanes@bmx.de')
        # Check first name
        self.assertEqual(normal_user_1.first_name, 'Jan')
        # Check last name
        self.assertEqual(normal_user_1.last_name, 'Parlesak')

        # Get the first normal user
        normal_user_1 = self.UserModel.objects.get(username='SönkFlug')
        # Check email
        self.assertEqual(normal_user_1.email, 'soenkehaenel@uni-goettingen.de')
        # Check first name
        self.assertEqual(normal_user_1.first_name, 'Sönke')
        # Check last name
        self.assertEqual(normal_user_1.last_name, 'Hänel')

        # Get the first normal user
        normal_user_1 = self.UserModel.objects.get(username='PaulDerGroße')
        # Check email
        self.assertEqual(normal_user_1.email, 'pwiepaul@gmail.com')
        # Check first name
        self.assertEqual(normal_user_1.first_name, 'Paul')
        # Check last name
        self.assertEqual(normal_user_1.last_name, 'Jarschke')
