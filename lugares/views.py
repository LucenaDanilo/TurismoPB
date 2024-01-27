from django.shortcuts import render,redirect
from lugares.models import City, Local,Location,Contact
from app.Forms import AddlocalForm

# Create your views here.

def landing_page_view(request):

    #puxa todas as cidades do Banco de dados
    locals = Local.objects.all()
    
    restaurant_counter = len(Local.objects.filter(category__name='Restaurantes'))
    hotel_counter = len(Local.objects.filter(category__name='Hotel'))
    hotel_counter = len(Local.objects.filter(category__name='Natureza'))
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
    return render(request, 'landing_page.html', {'locals': locals, 'restaurant_counter':restaurant_counter})

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
        locals = Local.objects.filter(location__localidade__icontains=search)

    return render(request,'lugares.html', {'locals': locals})



def add_local_view(request):
    

    if request.method == "POST":
        add_local_form = AddlocalForm(request.POST, request.FILES)

        if add_local_form.is_valid():
            add_local_form.save()
            return redirect('landing_page_view')
        

    else:
        add_local_form = AddlocalForm()
    
    return render(request,'add_local.html',{'add_local_form': add_local_form})




