from django.urls import path
from core.decorators import routes
from . import views

app_name = "produit"
urlpatterns = [path(url.lstrip('/'), view) for url, view in routes]
