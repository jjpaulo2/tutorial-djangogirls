from django.shortcuts import render
from django.http import HttpResponse
from .models import Postagem

# Create your views here.

def hello(request):
    return HttpResponse("<h3>Bem vindo(a) ao meu site!</h3>")

def index(request):
    return render(request, "blog/index.html")

def postagens(request):
    postagens = Postagem.objects.order_by("data_publicacao")
    return render(request, "blog/postagens.html", {"postagens": postagens})
