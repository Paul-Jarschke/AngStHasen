from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


# create a form that will be passed to the registration template using the django user registration form.
#the django registration form takes care of matching passwords and etc. The forms are classes that later will
# be converted into html and later also be used for the login process
def register(request):
    if request.method == 'POST':  # if we get a post request
        form = UserRegisterForm(request.POST)  # create the form with our own specified form
        if form.is_valid(): #check if form is valid
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}') # return a success message
            return redirect('login') # redirect to login page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'current_user': request.user}) #return the form
