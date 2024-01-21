from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class NossoForm(UserCreationForm):
    email = forms.CharField(
        label = ("email"),
    )

    lastname = forms.CharField(
        label = ("lastname"),
    )


def login_view(request):

    return render(request,'login.html', {'login_form': ''})

def register_view(request):

    if request.method == 'POST':
        user_form = NossoForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            print('valido')
            return redirect('base_test_view')
        else:
            print('js')
    else:
        user_form = NossoForm()

    return render(request,'register.html', {'user_form': user_form})