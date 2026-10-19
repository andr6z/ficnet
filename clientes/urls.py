from django.urls import path
from .views import home
from .views import teste

urlpatterns = [
    path('', home, name='home'),
    path('teste/', teste, name='teste')
]