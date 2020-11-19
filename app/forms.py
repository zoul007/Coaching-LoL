from django import forms
from .models import *
from django.forms import ValidationError


class AspiranteForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3,max_length=15)
    nombre_invocador = forms.CharField(min_length=4,max_length=15)

    def clean_correo(form):
        correo = form.cleaned_data["correo"]
        exist_correo = Aspirante.objects.filter(correo__iexact = correo).exists()

        if exist_correo:
            raise ValidationError("Este Correo ya está registrado")

        return correo

    def clean_nombre_invocador(self):
        nombre_invocador = self.cleaned_data["nombre_invocador"]
        exist_nombre_invocador = Aspirante.objects.filter(nombre_invocador__iexact = nombre_invocador).exists()

        if exist_nombre_invocador:
            raise ValidationError("Este Invocador ya está registrado")

        return nombre_invocador



    class Meta:
        model = Aspirante
        fields = ["nombre","correo","nombre_invocador","servidor","Liga"]

class ImageForm(forms.ModelForm):
   class Meta:
      model = Image
      fields = ['image','name']
