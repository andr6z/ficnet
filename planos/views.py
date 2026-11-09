from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from clientes.views import eh_funcionario
from .models import Plano
from .forms import PlanoForm

def lista_planos(request):
    planos = Plano.objects.filter(ativo=True)
    return render(request, 'planos.html', {'planos': planos})

@login_required(login_url='login')
@user_passes_test(eh_funcionario, login_url='area-cliente')
def novo_plano(request):
    if request.method == 'POST':
        form = PlanoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('planos')
    else:
        form = PlanoForm()
    return render(request, 'plano_form.html', {'form': form})

@login_required(login_url='login')
def contratar_plano(request, plano_id):
    plano = get_object_or_404(Plano, id=plano_id, ativo=True)
    if hasattr(request.user, 'perfil') and request.user.perfil.cliente:
        cliente = request.user.perfil.cliente
        cliente.plano = plano
        cliente.save()
    return redirect('area-cliente')