from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Evento, Convidado
from .forms import EventoForm, ConvidadoForm

class ConvidadoCreateView(CreateView):
    model = Convidado
    form_class = ConvidadoForm
    template_name = 'clube/convidado_form.html'
    success_url = '/'

class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'clube/evento_form.html'
    success_url = '/'
