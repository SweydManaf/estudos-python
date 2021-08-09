from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """A página inicial de Learning Log."""

    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Mostra todos os assuntos."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)


def check_topic_owner(request, topic):
    """Verifica se o usuário atual é o dono das requisições do tópico."""
    if topic.owner != request.user:
        raise Http404


@login_required
def topic(request, topic_id):
    """Mostra um único assunto e todas as suas entradas."""
    topic = Topic.objects.get(id=topic_id)
    # Garante que o assunto pertence ao usuário atual.
    check_topic_owner(request, topic)
    entries = topic.entry_set.order_by('-date_added')

    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Adiciona um novo assunto."""
    if request.method == 'POST':
        # Dados de POST submetidos; processa os dados.
        form = TopicForm(request.POST)
        # Verifica se são dados válidos.
        if form.is_valid():
            # Se for, cria uma instância com o tópico sem salvar
            # e liga esse tópico ao usuário atual.
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            # Salva os dados ligados ao usuário no banco de dados.
            new_topic.save()

            # Redireciona de volta para a página dos tópicos.
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    else:
        # Nenhum dado submetido, cria um formulário em branco.
        form = TopicForm()

    # Cria um contexto para renderizar no HTML.
    context = {'form': form}

    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Acrescenta uma nova entrada para um assunto em particular."""
    topic = Topic.objects.get(id=topic_id)
    # Garante que o assunto pertence ao usuário atual
    # antes de salvar a nova entrada.
    check_topic_owner(request, topic)

    if request.method == 'POST':
        # Dados de POST submetidos; processa os dados.
        form = EntryForm(data=request.POST)
        # Verifica se são dados válidos.
        if form.is_valid():
            # Se for, cria uma nova entrada sem salvar no banco de dados.
            new_entry = form.save(commit=False)
            # Liga o atributo topic de new_entry com o topic criado.
            new_entry.topic = topic
            # Salva os dados no banco de dados.
            new_entry.save()

            # Redireciona de volta para a página do tópico.
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))
    else:
        # Nenhum dado submetido, cria um formulário em branco.
        form = EntryForm()

    # Cria um contexto para renderizar no HTML.
    context = {'topic': topic, 'form': form}

    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edita uma entrada existente."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # Verifica se o usuário atual é o dono da entrada.
    check_topic_owner(request, topic)

    if request.method == 'POST':
        # Dados de POST submetidos; processa os dados.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))
    else:
        # Então vai ser a requisição inicial;
        # preenche previamente o formulário com a entrada atual.
        form = EntryForm(instance=entry)

    # Cria um contexto para renderizar no HTML.
    context = {'entry': entry, 'topic': topic, 'form': form}

    return render(request, 'learning_logs/edit_entry.html', context)
