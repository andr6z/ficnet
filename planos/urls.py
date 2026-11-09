from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_planos, name='planos'),
    path('novo/', views.novo_plano, name='novo-plano'),
    path('contratar/<int:plano_id>/', views.contratar_plano, name='contratar-plano'),
]