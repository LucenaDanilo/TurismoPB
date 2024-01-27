from django import forms
from lugares.models import Local,City, State, Contact, Location, Category
from django.contrib.auth.models import User
import requests



class AdduserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','phone','password']

class AddlocalForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    cep = forms.CharField(max_length=9)
    category = forms.ModelChoiceField(Category.objects.all())
    avaliation = forms.FloatField()
    price_range = forms.IntegerField()
    photo = forms.ImageField()
    

    def clean_avaliation(self):
        avaliation = self.cleaned_data['avaliation']
        if avaliation < 1 or avaliation > 5:
            self.add_error('avaliation', 'A avaliaçao deve estar entre 1 e 5')
        return avaliation
    
    def clean_cep(self):
        cep = self.cleaned_data['cep']
        cep.replace('-','')

        if len(cep) != 8 or cep.isnumeric() == False:
            self.add_error('cep', 'Digite um cep válido')
        return cep

    def save(self,user):


        def busca_endereco(cep):
            cep.replace('-','')
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            dados = response.json()
            print(dados)
            location = Location(
                logradouro = dados['logradouro'],
                bairro = dados['bairro'],
                localidade = dados['localidade'],
                uf = dados['uf'],
                cep = dados['cep'],
            )
            location.save()
            return location
        
        Endereco = busca_endereco(self.cleaned_data['cep'])
        
        local = Local(
            name = self.cleaned_data['name'],
            category = self.cleaned_data['category'],
            location = Endereco,
            description = self.cleaned_data['description'],
            avaliation = self.cleaned_data['avaliation'],
            price_range = self.cleaned_data['price_range'],
            photo = self.cleaned_data['photo'],
            user = user,
        )
        
        local.save()
        return local
    

class AddlocalModelForm(forms.ModelForm):
    def meta():
        model = Local
        fields = '__all__'