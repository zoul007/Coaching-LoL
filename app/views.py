from django.shortcuts import render
from .models import *
from django.forms import modelformset_factory

from .forms import AspiranteForm, CustUserCreationForm
from django.contrib import messages

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .serializers import AspiranteSerializer


# Create your views here.
class AspiranteViewset(viewsets.ModelViewSet):
    queryset = Aspirante.objects.all()
    serializer_class = AspiranteSerializer



def home(request):
    return render (request, 'app/home.html')


def galeria(request):
    return render (request, 'app/galeria.html')


def quienes_somos(request):
    return render (request, 'app/quienes_somos.html')


def registrate(request):
    data = {
        'form': AspiranteForm()
    }

    if request.method == 'POST':
        formulario = AspiranteForm(data=request.POST)
        if formulario.is_valid():

            formulario.save()
            messages.success(request, 'Registro Exitoso')

        else:
            data["form"] = formulario


    return render (request, 'app/registrate.html',data)


def image_gallery(request):
    images = Image.objects.all()
    print(images)
    return render(request, 'app/image_gallery.html', {'images': images})

def registro(request):
    data = {
        'form': CustUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Ingreso al sistema Exitoso")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html',data)
