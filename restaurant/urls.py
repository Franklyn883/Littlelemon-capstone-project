from django.urls import path
from . import views


urlpatterns = [
     path('', views.sayHello, name="sayhello"),
     path('home', views.home),
     path('menu/', views.MenuItemView.as_view(), name="menu"),
     path('menu/<int:pk>', views.SingleItemView.as_view,),
   
]