from django.contrib import admin
from lugares.models import City, Location, Contact, Local, State, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('logradouro',)
    search_fields = ('logradouro',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('telephone', 'email')
    search_fields = ('email',)

class LocalAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'location', 'contact')
    search_fields = ('name', 'category', 'location')

admin.site.register(Category,CategoryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Local, LocalAdmin)
