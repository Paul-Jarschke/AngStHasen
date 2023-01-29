from django.apps import AppConfig
from django.contrib.auth.models import User


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):

        # Admin user:
        try:  # such that 'unique'-condition for username will not be violated
            User.objects.create_superuser(username='LeonHase',
                                          email='leon@pythonexperts.com',
                                          password='notafraidofflying1999',
                                          first_name='Leon',
                                          last_name='Löppert')
        except:
            pass

        # Three normal users:
        try:
            User.objects.create_user(username='Janniboy_xD',
                                     email='janlovesplanes@bmx.de',
                                     password='ichmagflugzeuge_x3',
                                     first_name='Jan',
                                     last_name='Parlesak')
        except:
            pass

        try:
            User.objects.create_user(username='SönkFlug',
                                     email='soenkehaenel@uni-goettingen.de',
                                     password='appliedstatisticsftw',
                                     first_name='Sönke',
                                     last_name='Hänel')
        except:
            pass

        try:
            User.objects.create_user(username='PaulDerGroße',
                                     email='pwiepaul@gmail.com',
                                     password='lecker!paulanerspezi',
                                     first_name='Paul',
                                     last_name='Jarschke')
        except:
            pass
