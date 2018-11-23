from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h3>Bem vindo(a) ao meu site!</h3>")

def hello(request):
    return render(request, "blog/hello.html", {})
