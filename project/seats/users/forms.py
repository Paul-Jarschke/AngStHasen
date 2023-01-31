from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#specifying the forms for registering
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta: #keeps all configurations in one place
        model = User #whenever form validates a new User is created and saved
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2'] #field that will be shown
