from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def lista_planos(request):
    return render(request, 'planos.html')