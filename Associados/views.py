from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Associado
from .forms import AssociadoForm, DependenteForm
from django.db import transaction

class Associados_ListView(ListView):
    model = Associado 

class Associados_CreateView(CreateView):
    model = Associado
    form_class = AssociadoForm
    template_name = 'Associados/associado_form.html'
    success_url = reverse_lazy("Associados_ListView")

    def form_valid(self, form):
        context = self.get_context_data()
        dependentes = context['formset']
        with transaction.atomic():
            self.object = form.save()
            if dependentes.is_valid():
                dependentes.instance = self.object
                dependentes.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = DependenteForm(self.request.POST)
        else:
            data['formset'] = DependenteForm()
        return data

class Associados_UpdateView(UpdateView):
    model = Associado
    form_class = AssociadoForm
    template_name = 'Associados/associado_form.html'
    success_url = reverse_lazy("Associados_ListView")

    def form_valid(self, form):
        context = self.get_context_data()
        dependentes = context['formset']
        with transaction.atomic():
            self.object = form.save()
            if dependentes.is_valid():
                dependentes.instance = self.object
                dependentes.save()
            else:
                print(dependentes.errors)  # Adicione isso para verificar erros no console
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = DependenteForm(self.request.POST, instance=self.object)
        else:
            data['formset'] = DependenteForm(instance=self.object)
        return data

class Associados_DeleteView(DeleteView):
    model = Associado
    success_url = reverse_lazy("Associados_ListView")
