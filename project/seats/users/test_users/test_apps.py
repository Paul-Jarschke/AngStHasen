from django.contrib.auth import get_user_model
from django.apps import apps
from django.test import TestCase


class TestUsersConfig(TestCase):
    def setUp(self):
        self.UserModel = get_user_model()

    def test_default_auto_field(self):
        user_config = apps.get_app_config('users')
        self.assertEqual(user_config.default_auto_field, 'django.db.models.BigAutoField')

    def test_users_created(self):
        self.assertEqual(self.UserModel.objects.count(), 4)
        self.assertEqual(self.UserModel.objects.filter(is_staff=True).count(), 1)
        self.assertEqual(self.UserModel.objects.filter(is_superuser=True).count(), 1)

    def test_user_attributes(self):
        admin_user = self.UserModel.objects.get(username='LeonHase')
        self.assertEqual(admin_user.email, 'leon@pythonexperts.com')
        self.assertEqual(admin_user.first_name, 'Leon')
        self.assertEqual(admin_user.last_name, 'Löppert')

        normal_user_1 = self.UserModel.objects.get(username='Janniboy_xD')
        self.assertEqual(normal_user_1.email, 'janlovesplanes@bmx.de')
        self.assertEqual(normal_user_1.first_name, 'Jan')
        self.assertEqual(normal_user_1.last_name, 'Parlesak')

        normal_user_2 = self.UserModel.objects.get(username='SönkFlug')
        self.assertEqual(normal_user_2.email, 'soenkehaenel@uni-goettingen.de')
        self.assertEqual(normal_user_2.first_name, 'Sönke')
        self.assertEqual(normal_user_2.last_name, 'Hänel')

        normal_user_3 = self.UserModel.objects.get(username='PaulDerGroße')
        self.assertEqual(normal_user_3.email, 'pwiepaul@gmail.com')
        self.assertEqual(normal_user_3.first_name, 'Paul')
        self.assertEqual(normal_user_3.last_name, 'Jarschke')