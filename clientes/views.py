from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from .models import Cliente
from .forms import ClienteForm

def eh_funcionario(user):
    if not user.is_authenticated:
        return False
    if hasattr(user, 'perfil') and user.perfil.setor == 'CLIENTE':
        return False
    return True

def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
@user_passes_test(eh_funcionario, login_url='area-cliente')
def lista_clientes(request):
    busca = request.GET.get('q', '')
    clientes = Cliente.objects.select_related('plano').all()

    if busca:
        clientes = clientes.filter(
            Q(nome__icontains=busca) |
            Q(sobrenome__icontains=busca) |
            Q(cpf__icontains=busca)
        )

    return render(request, 'clientes.html', {'clientes': clientes, 'busca': busca})

@login_required(login_url='login')
@user_passes_test(eh_funcionario, login_url='area-cliente')
def novo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes-home')
    else:
        form = ClienteForm()

    return render(request, 'clientesForm.html', {'form': form})

@login_required(login_url='login')
@user_passes_test(eh_funcionario, login_url='area-cliente')
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes-home')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientesForm.html', {'form': form, 'cliente': cliente})

@login_required(login_url='login')
@user_passes_test(eh_funcionario, login_url='area-cliente')
def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes-home')

    return render(request, 'cliente_confirm_delete.html', {'cliente': cliente})