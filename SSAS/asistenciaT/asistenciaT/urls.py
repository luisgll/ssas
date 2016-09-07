__author__ = 'Luis Gabriel Liscano Lovera (ccidbcomputacion12@gmail.com)'
"""asistenciaT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from repgar.views import *
#from asistenciaT.views import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^home/',Home, name='home'),
    url(r'^repuesto/',repuesto, name='repuesto'),
    url(r'^registro/',registro, name='registro'),
    url(r'^prueba/',consulta, name='consulta'),
    url(r'^contacto/',contacto, name='contacto'),
    url(r'^gracias/',gracias, name='gracias'),
    url(r'^$',login,{'template_name':'login.html'},name='login'),
    url(r'^logout/',logout,{'template_name':'logout.html'},name='logout'),
    #url(r'^login/',login_page),
    #url(r'^login/',login,{'template_name':'base/index.html'},name='login'),

]
