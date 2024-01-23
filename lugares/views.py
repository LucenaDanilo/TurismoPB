from django.shortcuts import render
from lugares.models import City, Local,Location,Contact

# Create your views here.

def landing_page_view(request):

    #puxa todas as cidades do Banco de dados
    locals = Local.objects.all()
    
    
    #filtrando por propriedade
    # pernambuco = City.objects.filter(state__name="PE")

    #filtrando usando fucao ex: contains
    # joao_pessoa = City.objects.filter(name__contains = "Joao")


    #requisicao do usuario (url)
    search = request.GET.get('search')
    
    # if search != None:
    #     user_search = City.objects.filter(name__icontains = search) #contains(case sensitive) icontains(not case sensitive)
    #     return render(request, 'landing_page.html', {'cities': user_search})
    # else:
    return render(request, 'landing_page.html', {'locals': locals})
    



def base_test_view(request):
    return render(request, 'base_test.html', {})

def login_test_view(request):
    return render(request,'login_test.html',{})

def register_test_view(request):
    return render(request,'register_test.html',{})

def lugares_view(request):

    locals = Local.objects.all()

    search = request.GET.get('search')
    if search:
        locals = Local.objects.filter(category__name__icontains=search)

    return render(request,'lugares.html', {'locals': locals})

def cities_view(request):

    locals = Local.objects.all()

    search = request.GET.get('search')
    if search:
        locals = Local.objects.filter(location__city__name__icontains=search)

    return render(request,'lugares.html', {'locals': locals})








    cities = City.objects.all()

    search = request.GET.get('search')
    if search:
        cities = Local.objects.filter(location__city__name__icontains=search)

    return render(request,'cities.html', {'cities': cities})