from django.urls import path
from . import views

urlpatterns = [
     path('', views.sayHello, name="sayhello"),
     path('home', views.home)
]