from django.shortcuts import render
from django.http import HttpResponse
from core.decorators import route
from django.views import generic
from django.views.generic import TemplateView
from django.urls import get_resolver, reverse, NoReverseMatch

@route("", name="index")
def index(request):
    return render(request, "produit/index.html")

@route(path="hello/", name="hello")
def hello_view(request):
    return render(request, "produit/hello.jinja")

@route(path="aurevoir/", name="aurevoir")
def goodbye_view(request):
    return render(request, "produit/aurevoir.html")

@route(path="<int:id>/", name="test")
def id_view(request, id):
    return HttpResponse(f"bonjour {id}")

@route(path="test/", name="le chemin de test")
class IndexView(TemplateView):
    template_name = "produit/index.html"