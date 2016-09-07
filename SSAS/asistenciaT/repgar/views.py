from django.shortcuts import *

from .models import *


__author__ = 'Luis Gabriel Liscano Lovera (ccidbcomputacion12@gmail.com)'


# Create your views here.




def Home(request):
    name="Luis Liscano"
    return render_to_response('base/index.html',locals())



def consulta(request):
    DT=DatosTecnico.objects.all()
    return render_to_response('base/prueba.html',locals())



def repuesto(request):
    R=Repuesto.objects.all()
    name="Repuesto"
    return render_to_response('repuesto/repuesto.html',locals())


def registro(request):
    rg=Registro.objects.all()
    name="Registro"
    return render_to_response('registro/registro.html',locals())



def contacto(request):
    if request.method=='POST':#si el formulario es enviado
        form= Formulario(request.POST)
        if form.is_valid():#Si el formulario es valido se prosesan los datos
            return HttpResponseRedirect('gracias/')

    else:
        form=Formulario()
    return render_to_response('registro/registroUser.html',{'form':form})

def gracias(request):
    html='<html><head><title>Gracias SSAS</title></head><body><h1>Gracias por visitar XD <script type="text/javascript">alert("js en django")</script></h1></body></html>'
    return HttpResponse(html)
    #return render_to_response('practicajs6.html')