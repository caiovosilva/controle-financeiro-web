from django.shortcuts import render
from .models import LancamentosReceber
# def home(request):
#     return render(request, 'app/home.html', {})

def ver_lancamento_contas_receber(request):
    lancamentos = LancamentosReceber.objects.all()
    return render(request, 'app/ver_lancamento_contas_receber.html', {'lancamentos': lancamentos})
