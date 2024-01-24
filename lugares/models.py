from django.db import models
from PIL import Image


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='state', null=True)
    photo = models.ImageField(upload_to='cidades/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height != img.width:
            base_size = min(img.height, img.width)
            left = (img.width - base_size) / 2
            top = (img.height - base_size) / 2
            right = (img.width + base_size) / 2
            bottom = (img.height + base_size) / 2

            img = img.crop((left, top, right, bottom))

        img.save(self.photo.path)


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='city')

    def __str__(self):
        return self.rua
     

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    telephone = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.telephone
    

class Local(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category_name')
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='local_location')
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='local_contact')
    description = models.CharField(max_length=200, blank=True, null=True)
    avaliation = models.FloatField(blank=True, null=True)
    comments = models.CharField(max_length=200, blank=True, null=True)
    price_range = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='lugares/', blank=True, null=True)
    # opening_hours =

    def __str__(self) -> str:
        return self.name  
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)

        if img.height != img.width:
            base_size = min(img.height, img.width)
            left = (img.width - base_size) / 2
            top = (img.height - base_size) / 2
            right = (img.width + base_size) / 2
            bottom = (img.height + base_size) / 2

            img = img.crop((left, top, right, bottom))

        img.save(self.photo.path)
