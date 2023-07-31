from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHello(request):
    return HttpResponse('<h1 style="color:red text-align:center">Hello World<h1>')

def home(request):
    return render(request, 'restaurant/index.html',{})