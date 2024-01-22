from django.db import models

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name  

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='city')
     

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    telephone = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, null=True)
    

class Local(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='local_location')
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='local_contact')
    description = models.CharField(max_length=200, blank=True, null=True)
    avaliation = models.FloatField(blank=True, null=True)
    comments = models.CharField(max_length=200, blank=True, null=True)
    price_range = models.IntegerField(blank=True, null=True)
    # opening_hours =

    def __str__(self) -> str:
        return self.name  

