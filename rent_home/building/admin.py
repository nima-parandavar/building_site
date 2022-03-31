from django.contrib import admin
from .models import Building, Address
# Register your models here.

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('postal_code', 'state', 'city')

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('user', 'area', 'document_type', 'building_type', 'price', 'status')
    date_hierarchy = 'created'
    
    