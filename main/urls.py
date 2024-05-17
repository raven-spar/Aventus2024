from django.urls import path
from . import views

#Urlconf
urlpatterns = [
    path('', views.index),
]