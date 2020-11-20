from django.urls import path
from . import views
from.views import home, galeria, quienes_somos, registrate, registro

urlpatterns = [
    path('', home, name="home"),
    path('quienes_somos/', quienes_somos, name="quienes_somos"),
    path('registrate/', registrate, name="registrate"),
    path('image_gallery/', views.image_gallery, name='image_gallery'),
    path('registro/', registro , name="registro")
]
