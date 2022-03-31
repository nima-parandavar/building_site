from django.contrib import admin
from .models import RealEstateAgency
from django.utils.html import format_html

# Register your models here.
@admin.register(RealEstateAgency)
class REAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'agency_name', 'agency_phone', 'license_number', 'active_status')
    list_filter = ('user__is_active',)
    search_fields = ('license_number', 'national_number', 'user__username')

