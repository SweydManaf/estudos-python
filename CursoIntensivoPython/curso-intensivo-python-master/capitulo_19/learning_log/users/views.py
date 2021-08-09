from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Faz o cadastro de um novo usuário."""
    if request.method == 'POST':
        # Processa o formulário preenchido.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # Cria uma instância do novo usuário já salvo no banco de dados.
            new_user = form.save()
            # Faz login do usuário e o redireciona para a página inicial.
            authenticated_user = authenticate(
                username=new_user.username,
                password=request.POST['password1']
            )
            login(request, authenticated_user)

            return HttpResponseRedirect(reverse('learning_logs:index'))
    else:
        # Exibe o formulário de cadastro em branco.
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)
