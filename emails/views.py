from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
# Create your views here.


def enviar_email(mail):
    context = {'mail':mail}

    template = get_template('cuerpo.html')
    content = template.render(context)
    
    email = EmailMultiAlternatives(
        'Un correo de Prueba',
        'Envio de mail',
        settings.EMAIL_HOST_USER,
        [mail]
    )
    email.attach_alternative(content, 'text/html')
    email.send()


def envio_correo(request):
    if request.method == 'POST':
        mail = request.POST.get('email')

        enviar_email(mail)

    return HttpResponse('el correo fue enviado exitosamente')

def abrir_formulario(request):
    return render(request, 'envio.html')