from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_info, name='add_info'),
    path('get_info',views.get_info, name='get_info')
]