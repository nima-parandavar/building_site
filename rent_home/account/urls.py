from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('re_register/', views.re_register, name='re_register')
]

