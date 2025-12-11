from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ClientForm
from .models import Client
from django.shortcuts import get_object_or_404
from .forms import AvaliacaoForm
from .models import Avaliacao


@login_required
def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.criado_por = request.user
            client.save()
            return redirect('clientes:list')
    else:
        form = ClientForm()
    return render(request, 'clientes/client_form.html', {'form': form})


@login_required
def client_list(request):
    qs = Client.objects.filter(criado_por=request.user).order_by('-criado_em')
    # attach a computed status to each client based on latest Avaliacao
    for client in qs:
        latest = client.avaliacoes.order_by('-criado_em').first()
        if latest is None:
            client.status = 'Aguardando Avaliação'
        else:
            client.status = 'Aprovado' if latest.aprovado else 'Reprovado'
    return render(request, 'clientes/client_list.html', {'clients': qs})


@login_required
def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk, criado_por=request.user)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clientes:list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clientes/client_form.html', {'form': form, 'client': client})


@login_required
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk, criado_por=request.user)
    if request.method == 'POST':
        client.delete()
        return redirect('clientes:list')
    return render(request, 'clientes/client_confirm_delete.html', {'client': client})


@login_required
def create_avaliacao(request, client_pk):
    client = get_object_or_404(Client, pk=client_pk, criado_por=request.user)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            aval = form.save(commit=False)
            aval.client = client
            aval.avaliador = request.user
            aval.save()
            return redirect('clientes:list')
    else:
        form = AvaliacaoForm()
    return render(request, 'clientes/avaliacao_form.html', {'form': form, 'client': client})
