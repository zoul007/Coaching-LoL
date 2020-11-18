from django import forms
from .models import *

class AspiranteForm(forms.ModelForm):
    class Meta:
        model = Aspirante
        fields = ["nombre","correo","nombre_invocador","servidor","Liga"]
        
class ImageForm(forms.ModelForm):
   class Meta:
      model = Image
      fields = ['image','name']
