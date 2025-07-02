from django.urls import path
from core.decorators import routes
from . import views

app_name = "produit"
urlpatterns = [path(url.lstrip('/'), view, name=name) for url, view, name in routes]
