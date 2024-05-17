from django.urls import path
from . import views

#Urlconf
urlpatterns = [
    path('hello/', views.say_hello)
]