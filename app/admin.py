from django.contrib import admin
from .models import Clientes
from .models import Empresas
from .models import Fornecedores
from .models import PlanosDeContas
from .models import LancamentosReceber
from .models import FormasPagamento
from .models import ContasBancarias
from .models import BaixasPagar
from .models import BaixasReceber
from .models import LancamentosPagar
from .models import Tesouraria
from .models import TiposPessoa

admin.site.register(TiposPessoa)
admin.site.register(Clientes)
admin.site.register(Empresas)
admin.site.register(Fornecedores)
admin.site.register(PlanosDeContas)
admin.site.register(LancamentosReceber)
admin.site.register(FormasPagamento)
admin.site.register(ContasBancarias)
admin.site.register(BaixasPagar)
admin.site.register(BaixasReceber)
admin.site.register(LancamentosPagar)
admin.site.register(Tesouraria)