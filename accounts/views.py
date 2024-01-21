from django import forms
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.
class NossoForm(UserCreationForm):
    email = forms.EmailField(label="Email", max_length=254)
    lastname = forms.CharField(label="Sobrenome")

    class Meta:
        model = User
        fields = ("username", "email", "lastname",)

    def save(self, commit=True):
        user = super(NossoForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    

def login_view(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if (user is not None):
            login(request, user)
            return redirect('base_test_view')
        else:
            login_form = AuthenticationForm()   
    else: # get
        login_form = AuthenticationForm()   

    return render(request, 'login.html', {'login_form':login_form})



def register_view(request):

    if request.method == 'POST':
        user_form = NossoForm(request.POST)
        print(user_form)
        if user_form.is_valid():
            user_form.save()
            
            print('valido')
            return redirect('base_test_view')
        else:
            print('js')
    else:
        user_form = NossoForm()

    return render(request,'register.html', {'user_form': user_form})