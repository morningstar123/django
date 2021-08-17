from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from module import consultas



def datos(request):
    context={}
    datos=consultas.consulta_general()
    context['datos']=[datos.to_html(header=True, border="0",justify='center',index=False,escape=False)]
    return render(request, "index.html", context)

def informacion(request):
    context={}
    return render(request, "informacion.html", context)

def graficos(request):
    context={}
    return render(request, "graficos.html", context)