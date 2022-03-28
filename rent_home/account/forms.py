from django import forms
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from .models import RealEstateAgency

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control mb-3', 'autocomplete': 'on'}),
            'last_name': forms.TextInput(attrs={'class':'form-control mb-3', 'autocomplete': 'on'}),
            'username': forms.TextInput(attrs={'class':'form-control mb-3'}), 
            'email': forms.EmailInput(attrs={'class':'form-control mb-3', 'autocomplete': 'on'}), 
            'password': forms.PasswordInput(attrs={'class':'form-control mb-3'}, render_value=True)
        }
        labels = {'username':'Phone number'}
        help_texts = {'username':None}




class RERegister(forms.ModelForm):
    class Meta:
        model = RealEstateAgency
        exclude = ('user',)
        widgets = {
            'national_number': forms.NumberInput(attrs={'class':'form-control mb-3'}),
            'license_number': forms.NumberInput(attrs={'class':'form-control mb-3'}),
            'license_document': forms.FileInput(attrs={'class':'form-control mb-3'}),
            'agency_name': forms.TextInput(attrs={'class':'form-control mb-3'}),
            'agency_phone': forms.NumberInput(attrs={'class':'form-control mb-3'}),
            'address': forms.TextInput(attrs={'class':'form-control mb-3'}),
        }
    
    captcha = ReCaptchaField(
        label='',
        widget=ReCaptchaV2Checkbox
    )