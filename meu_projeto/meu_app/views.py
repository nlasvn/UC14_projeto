from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def minha_view(_request):
    return HttpResponse("Hello, world!")


def oi(request):
    return render(request, "meu_app/index.html")
