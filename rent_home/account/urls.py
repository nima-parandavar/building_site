from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('re_register/', views.re_register, name='re_register'),

    path('login/', views.login_, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/edit_info/', views.edit_info, name='edit_info'),
    path('dashboard/change_password/', views.change_password, name = 'change_password')
]

