from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_usuario, name='login'),
    path('sair/', views.logout_usuario, name='logout'),
    path('minha-conta/', views.area_cliente, name='area-cliente'),
]