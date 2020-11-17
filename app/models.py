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
    correo = models.CharField(max_length = 30)
    nombre_invocador = models.CharField(max_length = 15)
    servidor = models.ForeignKey(Server, on_delete =models.PROTECT)
    Liga = models.ForeignKey(Liga, on_delete =models.PROTECT)

    def __str__(self):
        return self.nombre
