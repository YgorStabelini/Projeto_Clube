from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Fornecedor

class Fornecedor_ListView(ListView):
    model = Fornecedor

class Fornecedor_CreateView(CreateView):
    model = Fornecedor
    fields = fields = ['nome_razao_social', 'endereco', 'bairro', 'numero', 'cep', 'cidade', 'uf', 'telefone','celular','email','facebook','instagram','contato']
    success_url = reverse_lazy("Fornecedor_ListView")

class Fornecedor_UpdateView(UpdateView):
    model = Fornecedor
    fields = fields = ['nome_razao_social', 'endereco', 'bairro', 'numero', 'cep', 'cidade', 'uf', 'telefone','celular','email','facebook','instagram','contato']
    success_url = reverse_lazy("Fornecedor_ListView")

class Fornecedor_DeleteView(DeleteView):
    model = Fornecedor
    success_url = reverse_lazy("Fornecedor_ListView")