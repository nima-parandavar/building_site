from django.http import HttpRequest
from django.shortcuts import redirect, render
from .forms import RegisterForm, RERegister
from django.contrib.messages import add_message, SUCCESS
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import RealEstateAgency


# Create your views here.

def register(request:HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = make_password(form.cleaned_data['password'])
            print(password)
            user:User = form.save(commit=False)
            user.password = password
            user.is_active = True
            user.save()

            login(request, user)

            add_message(
                request,
                SUCCESS,
                'Congratolation, You are registered successfully',
                'alert alert-success',
                False
            )

            return redirect('account:dashboard')

    else:
        form = RegisterForm()
    
    context={'form':form}
    return render(request, 'account/register.html', context)


def re_register(request:HttpRequest):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        re_form = RERegister(request.POST, request.FILES)

        if user_form.is_valid() and re_form.is_valid():
            password = make_password(user_form.cleaned_data['password'])
            user:User = user_form.save(commit=False)
            user.password = password
            user.is_active = False
            user.save()

            re_user:RealEstateAgency = re_form.save(commit=False)
            re_user.user = user
            re_user.save()

            add_message(
                request,
                SUCCESS,
                'Thanks for joining us, your account will be active after it confirm.',
                extra_tags='alert alert-success mb-3',
                fail_silently=False
            )
        
    else:
        user_form = RegisterForm()
        re_form = RERegister()

    context = {'user_form': user_form, 're_form':re_form}
    return render(request, 'account/re_register.html', context)


@login_required
def dashboard(request:HttpRequest):
    return render(request, 'account/dashboard.html')