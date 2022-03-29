from django import forms
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import UsernameField
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

class LoginForm(forms.Form):
    username = UsernameField(
        label='Phone number',
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}, render_value=True)
    )

class EditInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control mb-3', 'autocomplete': 'on'}),
            'last_name': forms.TextInput(attrs={'class':'form-control mb-3', 'autocomplete': 'on'}),
            'username': forms.TextInput(attrs={'class':'form-control mb-3'}), 
            'email': forms.EmailInput(attrs={'class':'form-control mb-3', 'autocomplete': 'on'}), 
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}))

    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}))

