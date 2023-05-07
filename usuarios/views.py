from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .models import Personas



# Create your views here.

def enviar_email(mail):
    context = {'mail':mail}

    template = get_template('cuerpo.html')
    content = template.render(context)
    
    email = EmailMultiAlternatives(
        'Desarrollador Back-End',
        'Desarrollador Back-End',
        settings.EMAIL_HOST_USER,
        [mail],
        cc = ['lazaroflorez79@gmail.com']
    )
    email.attach_alternative(content, 'text/html')
    email.send()

def suscripcion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        usuario = Personas(nombre=nombre, email=email)
        usuario.save()
        enviar_email(email)
        return render(request, 'usuario_creado.html', {'nombre':nombre, 'email':email})
    return render(request, 'plantilla.html')


def IniciarSesion(request):
    return render(request, 'Iniciar_sesion.html')


def eliminar_registros(request):
    Personas.objects.all().delete()
    '''
    TRUNCATE TABLE usuarios_personas RESTART IDENTITY CASCADE;
    este codigo se utiliza para reiniciar los pk desde el comando sql
    '''
    return HttpResponse('Los registros fueron eliminados exitosamente')

