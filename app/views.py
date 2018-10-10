import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import LancamentosReceber
from django.shortcuts import get_object_or_404
from .forms import LancamentosReceberForm
from django.shortcuts import redirect

def home(request):
    return render(request, 'app/home.html', {})

def lancamento_receber_list(request):
    lancamentos = LancamentosReceber.objects.all()
    return render(request, 'app/lancamento_receber_list.html', {'lancamentos': lancamentos})

def lancamento_receber_edit(request, pk):
    lancamento = get_object_or_404(LancamentosReceber, pk=pk)
    if request.method == "POST":
        form = LancamentosReceberForm(request.POST, instance=lancamento)
        if form.is_valid():
            lancamento = form.save(commit=False)
            lancamento.save()
            return redirect('lancamento_receber_list')
    else:
        form = LancamentosReceberForm(instance=lancamento)
    return render(request, 'app/lancamento_receber_edit.html', {'form': form})

def lancamento_receber_edit(request):
    if request.method == "POST":
        form = LancamentosReceberForm(request.POST)
        if form.is_valid():
            lancamento = form.save(commit=False)
            lancamento.save()
            return redirect('lancamento_receber_list')
    else:
        form = LancamentosReceberForm()
    return render(request, 'app/lancamento_receber_edit.html', {'form': form})

def delete_lancamento_receber(request,pk):
   u = LancamentosReceber.objects.get(pk=pk).delete()
   return redirect('lancamento_receber_list')

def relatorio_lancamentos_receber(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="lancamentos_a_receber.csv"'

    writer = csv.writer(response)
    writer.writerow(['Cliente', 'Empresa', 'Data de Vencimento', 'Data de Emissão', 'Valor do Titulo', 'Numero do Documento'])

    for lancamento in LancamentosReceber.objects.all():
        writer.writerow([lancamento.Cliente, lancamento.Empresa, lancamento.data_Vencimento, lancamento.data_Emissao, lancamento.valor_Titulo, lancamento.numero_Documento])

    return response