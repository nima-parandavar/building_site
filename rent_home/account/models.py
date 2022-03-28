from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RealEstateAgency(models.Model):
    user:User = models.OneToOneField(User, models.CASCADE, related_name='real_estate_agency')

    national_number = models.PositiveIntegerField(blank=False, unique=True)

    license_number = models.PositiveIntegerField(blank=False, unique=True)
    license_document = models.ImageField(upload_to = 'media/%Y/%m/%d')

    agency_name = models.CharField(max_length=150, blank=False)
    agency_phone = models.CharField(max_length=11, blank=False)
    address = models.CharField(max_length=250, blank=False)

    def __str__(self) -> str:
        return self.agency_name

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def active_status(self):
        if self.user.is_active:
            return 'Active'
        else:
            return 'Disactive'

