from django.db import models

# Create your models here.

class Liga(models.Model):
    nombre = models.CharField(max_length = 20)

    def __str__(self):
        return self.nombre

class Server(models.Model):
    nombre = models.CharField(max_length = 20)

    def __str__(self):
        return self.nombre


class Aspirante(models.Model):
    nombre = models.CharField(max_length = 15)
    correo = models.EmailField()
    nombre_invocador = models.CharField(max_length = 15)
    servidor = models.ForeignKey(Server, on_delete =models.PROTECT)
    Liga = models.ForeignKey(Liga, on_delete =models.PROTECT)

    def __str__(self):
        return self.nombre


class Image(models.Model):
    image = models.ImageField(upload_to = 'galeria')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
