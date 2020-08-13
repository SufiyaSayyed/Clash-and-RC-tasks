from django.urls import path
from part2 import views

urlpatterns = [
    path('', views.profile, name='profile'), 
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]