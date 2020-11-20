from django.urls import path

from django.contrib.auth.views import (
PasswordResetView, # suggestion: PasswordResetView
PasswordResetDoneView,
PasswordResetConfirmView,
PasswordResetCompleteView
)
from django.contrib.auth import views as auth_views
from . import views
from.views import home, galeria, quienes_somos, registrate, registro

urlpatterns = [
    path('', home, name="home"),
    path('quienes_somos/', quienes_somos, name="quienes_somos"),
    path('registrate/', registrate, name="registrate"),
    path('image_gallery/', views.image_gallery, name='image_gallery'),
    path('registro/', registro , name="registro"),
    path('reset-password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
<<<<<<< HEAD

    #path('reset_password/',
    #PasswordResetView.as_view(template_name="registration/password_reset.html"),
    #name="reset_password"),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name='password_reset'),

    path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',
    PasswordResetConfirmView, name='password_reset_confirm'),
=======
    path('reset-password/', PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView, name='password_reset_confirm'),
    path('reset-password-complete/', PasswordResetCompleteView, name='password_reset_complete'),
>>>>>>> 8831daed8dccee3c2719cc1795fc839df3baa312

]
