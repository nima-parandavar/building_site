from django import forms
from .models import Building, Address
from django.utils.timezone import datetime

class AddressForm(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = '__all__'
        widgets = {
            'state': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'city': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'street': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'plate': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'postal_code': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'full_address': forms.TextInput(attrs={'class':'form-control mb-3'}),
        }

class BuildingForm(forms.ModelForm):
    
    class Meta:
        model = Building
        exclude = ('user', 'address', 'status')
        widgets = {
            'area': forms.NumberInput(attrs={'class':'form-control mb-3'}),
            'rooms': forms.NumberInput(attrs={'class':'form-control mb-3'}),
            'baths': forms.NumberInput(attrs={'class':'form-control mb-3'}) ,
            'with_home_appliances': forms.CheckboxInput(attrs={'class':'form-checkbox mb-3'}),
            'floor': forms.NumberInput(attrs={'class':'form-control mb-3'}) ,
            'building_type': forms.Select(attrs={'class':'form-select mb-3'}),
            'document_type':forms.Select(attrs={'class':'form-select mb-3'}) ,
            'construction_date': forms.SelectDateWidget(years=range(1980, datetime.today().year), attrs={'class':'form-select mb-3'}),
            'price': forms.NumberInput(attrs={'class':'form-control mb-3'}) ,
            'description': forms.TextInput(attrs={'class':'form-control mb-3'}) ,
            'picture': forms.FileInput(attrs={'class':'form-control mb-3'}) ,
            'title': forms.TextInput(attrs={'class':'form-control mb-3'}) ,
        }
        

class FilterForm(forms.Form):
    CITIES = tuple((obj.city, obj.city) for obj in Address.objects.all())
    STATES = tuple((obj.state, obj.state) for obj in Address.objects.all())
    STREETS = tuple((obj.street, obj.street) for obj in Address.objects.all())
    BUILDING_TYPE = (
        ('R', 'Residential'),
        ('V', 'Villa'),
        ('C', 'Commercial')
    )

    state = forms.ChoiceField(
        choices=STATES,
        required=False,
        widget=forms.Select(attrs={'class':'form-select'})
    )

    city = forms.ChoiceField(
        choices=CITIES, 
        required=False,
        widget=forms.Select(attrs={'class':'form-select'}),
    )

    street = forms.ChoiceField(
        choices=STREETS, 
        required=False,
        widget=forms.Select(attrs={'class':'form-select'}),
    )

    building_type = forms.ChoiceField(
        choices=BUILDING_TYPE, 
        required=False,
        widget=forms.Select(attrs={'class':'form-select'}),
    )

    price = forms.IntegerField(
        max_value=1000000,
        min_value=0,
        required=False,
        widget=forms.NumberInput(attrs={'type':'range', 'class':'form-range'})
    )
