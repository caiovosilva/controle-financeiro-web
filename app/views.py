from django.shortcuts import render
from .models import LancamentosReceber
from django.shortcuts import get_object_or_404
from .forms import LancamentosReceberForm
from django.shortcuts import redirect
# def home(request):
#     return render(request, 'app/base.html', {})

def lancamento_receber_list(request):
    lancamentos = LancamentosReceber.objects.all()
    return render(request, 'app/lancamento_receber_list.html', {'lancamentos': lancamentos})

def lancamento_receber_edit(request, pk):
    if request.method == "POST":
        form = LancamentosReceberForm(request.POST)
        if form.is_valid():
            lancamento = form.save(commit=False)
            lancamento.save()
            return redirect('lancamento_receber_list')
    else:
        form = LancamentosReceberForm()
    lancamento = get_object_or_404(LancamentosReceber, pk=pk)
    return render(request, 'app/lancamento_receber_edit.html', {'lancamento': lancamento, 'form': form})