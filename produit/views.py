from django.shortcuts import render
from django.http import HttpResponse
from core.decorators import route
from django.views import generic
from django.views.generic import TemplateView

@route("")
def index(request):
    return HttpResponse("test")

@route("hello/")
def hello_view(request):
    return HttpResponse("Bonjour depuis une vue auto-routée !")

@route("aurevoir/")
def goodbye_view(request):
    return HttpResponse("Au revoir !")

@route("<int:id>/")
def id_view(request, id):
    return HttpResponse(f"bonjour {id}")

@route("test/")
class IndexView(TemplateView):
    template_name = "produit/index.html"