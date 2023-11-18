from django import forms
from django.forms.models import inlineformset_factory
from .models import Associado, Dependente

class DependenteForm(forms.ModelForm):
    class Meta:
        model = Dependente
        fields = ['nome', 'cpf', 'rg', 'data_nascimento', 'tipo_vinculo']

DependenteFormSet = inlineformset_factory(Associado, Dependente, form=DependenteForm, extra=1, can_delete=True)

class AssociadoForm(forms.ModelForm):       
    class Meta:
        model = Associado
        fields = ['nome', 'endereco', 'bairro', 'cep', 'complemento', 'cidade', 'uf', 'telefone', 'celular', 'email', 'facebook', 'instagram', 'cpf', 'rg', 'data_nascimento', 'tipo_associacao']
    
    dependentes = DependenteFormSet()
