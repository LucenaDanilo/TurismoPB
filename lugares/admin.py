from django.contrib import admin
from lugares.models import City, Location, Contact, Local 

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'city')
    search_fields = ('city',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('telephone', 'email')
    search_fields = ('email',)

class LocalAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'location', 'contact')
    search_fields = ('name', 'category', 'location')

admin.site.register(City, CityAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Local, LocalAdmin)
