from django.contrib import admin
from .models import *
# Register your models here.


class AspiranteAdmin(admin.ModelAdmin):
    list_display = ["nombre","nombre_invocador","correo","servidor","Liga"]
    list_editable = ["Liga"]
    search_fields = ["nombre_invocador", "correo", "nombre"]
    list_filter =  ["Liga","servidor"]
    list_per_page = 10

admin.site.register(Aspirante, AspiranteAdmin)
admin.site.register(Liga)
admin.site.register(Server)
admin.site.register(Image)
