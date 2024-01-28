from django.shortcuts import render,redirect
from lugares.models import City, Local,Location,Contact
from app.Forms import AddlocalForm
from django.views import View
from django.views.generic import ListView

# Create your views here.


    

class landing_pageView(View):
    def get(self, request):
        locals = Local.objects.all()
        restaurant_counter = len(Local.objects.filter(category__name__icontains='Restaurantes'))
        hotel_counter = len(Local.objects.filter(category__name__icontains='Hotel'))
        natureza_counter = len(Local.objects.filter(category__name__icontains='Natureza'))
        cultura_counter = len(Local.objects.filter(category__name__icontains='Cultura'))
        museu_counter = len(Local.objects.filter(category__name__icontains='Museus'))
        
        return render(request, 'landing_page.html', {'locals': locals, 'restaurant_counter':restaurant_counter,'hotel_counter':hotel_counter,'natureza_counter':natureza_counter,'cultura_counter':cultura_counter,'museu_counter':museu_counter})
    
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

# class lugaresView(ListView):
#     model = Local


def cities_view(request):

    locals = Local.objects.all()

    search = request.GET.get('search')
    if search:
        locals = Local.objects.filter(location__localidade__icontains=search)

    return render(request,'lugares.html', {'locals': locals})



class add_localView(View):
    def get(self, request):
        add_local_form = AddlocalForm()
        return render(request,'add_local.html',{'add_local_form': add_local_form})
    
    def post(self,request):
        add_local_form = AddlocalForm(request.POST, request.FILES)

        if add_local_form.is_valid():
            add_local_form.save(request.user.username)
            return redirect('landing_page_view')
        return render(request,'add_local.html',{'add_local_form': add_local_form})