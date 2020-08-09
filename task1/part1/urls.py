from django.urls import path
from . import views

urlpatterns = [
    path('', views.num, name='numbers from 1-20'),
    path('printn',views.printn, name='printn')
]