from typing import Generic, List
from django import db
from django.db.models.base import Model
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from gameturbo.forms import ClienteForm
from locadora.models import Cliente
from gameturbo.formsjogo import JogoForm
from locadora.models import Jogo
from django.contrib import messages

from django.core.paginator import Paginator


# View Cliente.

def listarcliente(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Cliente.objects.filter(nome__icontains=search)
    else:
        data['db'] = Cliente.objects.all()
        all=Cliente.objects.all()
        paginator = Paginator(all, 7)
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)
    return render(request, 'listarcliente.html', data)

def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Cliente.objects.filter(nome__icontains=search)
    else:
         data['db'] = Cliente.objects.all()

    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = ClienteForm
    return render(request, 'form.html', data)

def create(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('form')

def view(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    data['form'] = ClienteForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('listarcliente')

def delete(request, pk):
    db = Cliente.objects.get(pk=pk)
    db.delete()

    messages.info(request, 'Cliente deletado com sucesso')
    return redirect('listarcliente')

# View Jogo.
def formjogo(request):
    data = {}
    data['formjogo'] = JogoForm
    return render(request, 'formjogo.html', data)

def createjogo(request):
    formjogo = JogoForm(request.POST or None)
    if formjogo.is_valid():
        formjogo.save()
        messages.info(request, 'Jogo acrescentado com sucesso')
        return redirect('formjogo')

def viewjogo(request, pk):
    data = {}
    data['db'] = Jogo.objects.get(pk=pk)
    return render(request, 'viewjogo.html', data)

def editjogo(request, pk):
    data = {}
    data['db'] = Jogo.objects.get(pk=pk)
    data['formjogo'] = JogoForm(instance=data['db'])
    return render(request, 'formjogo.html', data)

def updatejogo(request, pk):
    data = {}
    data['db'] = Jogo.objects.get(pk=pk)
    formjogo = JogoForm(request.POST or None, instance=data['db'])
    if formjogo.is_valid():
        formjogo.save()
    messages.info(request, 'Jogo atualizado com sucesso')
    return redirect('listarjogo')

def deletejogo(request, pk):
    db = Jogo.objects.get(pk=pk)
    db.delete()
    messages.info(request, 'Jogo deletado com sucesso')
    return redirect('listarjogo')


def listarjogo(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Jogo.objects.filter(titulo__icontains=search)
    else:
        data['db'] = Jogo.objects.all()
        all=Jogo.objects.all()
        paginator = Paginator(all, 7)
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)
    return render(request, 'listarjogo.html', data)