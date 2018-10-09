# forms.py
from django import forms

from .models import LancamentosReceber

class LancamentosReceberForm(forms.ModelForm):

    class Meta:
        model = LancamentosReceber
        fields = ('Cliente', 'Empresa','data_Vencimento','data_Emissao','valor_Titulo','numero_Documento',)