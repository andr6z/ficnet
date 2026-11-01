from django.urls import path
from .views import home, lista_clientes
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='clientes-home'),
    path('novo/', views.novo_cliente, name='novo-cliente'),
    path('editar/<int:id>/', views.editar_cliente, name='editar-cliente'),
    path('excluir/<int:id>/', views.excluir_cliente, name='excluir-cliente'),
]