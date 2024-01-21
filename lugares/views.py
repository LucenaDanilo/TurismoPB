from django.shortcuts import render

# Create your views here.

def base_test_view(request):
    return render(request, 'base_test.html', {})

def login_test_view(request):
    return render(request,'login_test.html',{})

def register_test_view(request):
    return render(request,'register_test.html',{})