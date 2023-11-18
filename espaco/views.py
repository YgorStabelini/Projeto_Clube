from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import EspacoLocavel

class EspacoLocavel_ListView(ListView):
    model = EspacoLocavel

class EspacoLocavel_CreateView(CreateView):
    model = EspacoLocavel
    fields = ['nome', 'tamanho', 'capacidade_pessoas', 'data_construcao_aquisicao', 'locavel']
    success_url = reverse_lazy("EspacoLocavel_ListView")

class EspacoLocavel_UpdateView(UpdateView):
    model = EspacoLocavel
    fields = ['nome', 'tamanho', 'capacidade_pessoas', 'data_construcao_aquisicao', 'locavel']
    success_url = reverse_lazy("EspacoLocavel_ListView")

class EspacoLocavel_DeleteView(DeleteView):
    model = EspacoLocavel
    success_url = reverse_lazy("EspacoLocavel_ListView")