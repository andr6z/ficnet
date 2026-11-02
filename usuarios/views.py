from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_usuario(request):
    if request.method == 'POST':
        usuario_digitado = request.POST.get('username')
        senha_digitada = request.POST.get('password')

        user = authenticate(request, username=usuario_digitado, password=senha_digitada)

        if user is not None:
            login(request, user)
            
            if hasattr (user, 'perfil') and user.perfil.setor == 'CLIENTE':
                return redirect('area-cliente')
            return redirect('clientes-home')  
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login.html')

def logout_usuario(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def area_cliente(request):

    cliente = getattr(request.user.perfil, 'cliente', None) if hasattr(request.user, 'perfil') else None
    return render(request, 'area_cliente.html', {'cliente': cliente})

