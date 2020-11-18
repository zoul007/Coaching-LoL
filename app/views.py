from django.shortcuts import render


# Create your views here.

def home(request):
    return render (request, 'app/home.html')

def galeria(request):

    return render (request, 'app/galeria.html')


def quienes_somos(request):
    return render (request, 'app/quienes_somos.html')

def registrate(request):
    return render (request, 'app/registrate.html')
