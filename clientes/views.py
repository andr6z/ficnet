from django.shortcuts import render, redirect, get_object_or_404
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

    return render(request, 'clientes_form.html', {'form': form})


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)  
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes-home')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes_form.html', {'form': form, 'cliente': cliente})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()  
        return redirect('clientes-home')

    return render(request, 'cliente_confirm_delete.html', {'cliente': cliente})