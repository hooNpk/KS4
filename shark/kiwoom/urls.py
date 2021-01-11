from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('today', views.today, name='today')
]