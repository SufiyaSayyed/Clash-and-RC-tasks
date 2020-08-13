from django.urls import path
from part1 import views

urlpatterns = [
    path('', views.add, name='add'),
    path('find',views.find, name='find')   
]