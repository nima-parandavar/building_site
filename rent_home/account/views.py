from django.http import HttpRequest
from django.shortcuts import redirect, render
from .forms import RegisterForm, RERegister, LoginForm, EditInfoForm, ChangePasswordForm
from django.contrib.messages import add_message, SUCCESS, WARNING, ERROR
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import RealEstateAgency
from django.core.exceptions import ObjectDoesNotExist


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


def login_(request:HttpRequest):
    user = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd.get('username')
            try:
                user:User = User.objects.get(username = username)
                if check_password(cd.get('password'), user.password):
                    login(request, user)
                    return redirect('account:dashboard')
                else:
                    add_message(
                    request,
                    ERROR,
                    'Your password is not correct, click on forget my password to reset it.',
                    'alert alert-danger',
                )


            except ObjectDoesNotExist:
                add_message(
                    request,
                    WARNING,
                    'You are not sign up yet',
                    'alert alert-warning',
                )
                return redirect('account:login')
            
            
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'account/login.html', context)

@login_required
def dashboard(request:HttpRequest):
    return render(request, 'account/dashboard.html')

@login_required
def edit_info(request:HttpRequest):
    if request.method == 'POST':
        form = EditInfoForm(data = request.POST, instance=request.user)
        if form.is_valid():
            form.save(commit=True)
            
            add_message(
                request,
                SUCCESS,
                'Your info change successfully',
                'alert alert-success mb-3',
                False
            )

            return redirect('account:dashboard')
    else:
        form = EditInfoForm(instance=request.user)
    context = {'form':form}
    return render(request, 'account/edit_info.html', context)

@login_required
def change_password(request:HttpRequest):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            if check_password(cd.get('current_password'), request.user.password) and cd.get('new_password') == cd.get('confirm_password'):
                user:User = User.objects.get(username=request.user.username)
                user.password = make_password(cd.get('new_password'))
                user.save(update_fields=['password'])

                logout(request)

                add_message(
                    request,
                    SUCCESS,
                    'Your password change successfully, log in again',
                    'alert alert-success',
                    False
                )

                return redirect('account:login')

                
    else:
        form = ChangePasswordForm()
    context = {'form': form}
    return render(request, 'account/change_password.html', context)