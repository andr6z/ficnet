from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def home(request):
    return render(request, 'home.html')

def lista_clientes(request):
    clientes = Cliente.objects.select_related('plano').all()
    return render(request, 'clientes.html', {'clientes': clientes})

def novo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('clientes-home')  
    else:
        form = ClienteForm()

    return render(request, 'clientesForm.html', {'form': form})