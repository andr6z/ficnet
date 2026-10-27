from django.urls import path
from .views import home, lista_clientes

urlpatterns = [
    path('', lista_clientes, name='clientes'),
]