from django.urls import path
from .views import home, lista_clientes

urlpatterns = [
    path('', home, name='home'),
    path('clientes/', lista_clientes, name='clientes-home'),
]