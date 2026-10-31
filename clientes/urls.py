from django.urls import path
from .views import home, lista_clientes
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='clientes-home'),
    path('novo/', views.novo_cliente, name='novo-cliente'),
]