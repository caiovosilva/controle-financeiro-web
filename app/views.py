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
