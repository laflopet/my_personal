"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import inicio
from usuarios.views import suscripcion, IniciarSesion, eliminar_registros
from emails.views import enviar_email, envio_correo, abrir_formulario


urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('suscripcion/', suscripcion, name='suscripcion'),
    path('usuario/', suscripcion, name='suscripcion'),
    path('login/', IniciarSesion),
    path('eliminar/registros', eliminar_registros, name='eliminar_registros'),
    path('enviar_email', envio_correo, name='enviar_email'),
    path('formulario/', abrir_formulario, name='abrir_formulario')
]