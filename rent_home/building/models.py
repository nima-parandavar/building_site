from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    plate = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    full_address = models.TextField()

    def __str__(self):
        return self.postal_code

class Building(models.Model):
    BUILDING_TYPE = (
        ('R', 'Residential'),
        ('V', 'Villa'),
        ('C', 'Commercial')
    )

    DOCUMENT_TYPE = (
        ('rent', 'Rent'),
        ('sell', 'For sell')
    )

    user = models.ForeignKey(User, models.CASCADE, related_name='the_buildings')
    title = models.CharField(max_length=200, null=True)

    area = models.PositiveIntegerField(blank=False, null=False)
    rooms = models.PositiveIntegerField(blank=False, null=False)
    baths = models.PositiveIntegerField(blank=False, null=False)

    with_home_appliances = models.BooleanField(default=False, blank=False, null=False)
    building_type = models.CharField(choices=BUILDING_TYPE, default='R', max_length=10)

    floor = models.PositiveIntegerField(default=0, blank=False, null=False)
    document_type = models.CharField(choices=DOCUMENT_TYPE, default='rent', max_length=10)

    construction_date = models.DateField()
    price = models.DecimalField(decimal_places=3, max_digits=1000000)

    address = models.OneToOneField(Address, models.CASCADE, related_name='building_address')
    description = models.TextField(blank=True)

    picture = models.ImageField(upload_to="%Y/%m/%d", blank=True)

    status = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.user)
    
    