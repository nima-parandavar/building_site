from django.urls import path
from . import views
app_name = 'bulding'

urlpatterns = [
    path('add_new_building/', views.add_new_building, name='add_new_building'),
    path('the_buildings/', views.the_buildings, name='the_buildings'),
    path('the_buildings/<int:pk>/', views.detail, name='detail'),
]
