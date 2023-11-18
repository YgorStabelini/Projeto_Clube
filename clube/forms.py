from django import forms
from .models import Evento, Convidado

class ConvidadoForm(forms.ModelForm):
    class Meta:
        model = Convidado
        fields = '__all__'

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
