from django import forms
from lugares.models import Local,City, State, Contact, Location, Category

class AddlocalForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    cep = forms.IntegerField()
    category = forms.ModelChoiceField(Category.objects.all())
    avaliation = forms.FloatField()
    price_range = forms.IntegerField()
    photo = forms.ImageField()

    def save(self):
        local = Local(
            name = self.cleaned_data['name'],
            category = self.cleaned_data['category'],
            cep = self.cleaned_data['cep'],
            description = self.cleaned_data['description'],
            avaliation = self.cleaned_data['avaliation'],
            price_range = self.cleaned_data['price_range'],
            photo = self.cleaned_data['photo'],
        )
        local.save()
        return local