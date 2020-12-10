from .models import Aspirante
from rest_framework import serializers

class AspiranteSerializer (serializers.ModelSerializer):
    nombre_servidor = serializers.CharField (read_only=True, source ="servidor.nombre")
    nombre_liga = serializers.CharField (read_only=True, source ="Liga.nombre")

    class Meta:
        model = Aspirante
        fields = ('nombre_invocador','nombre_liga', 'nombre_servidor' )
        depth = 3
