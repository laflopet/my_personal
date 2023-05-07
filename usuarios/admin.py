from django.contrib import admin

# Register your models here.
from usuarios.models import Personas

admin.site.register(Personas)