from django.db import models
from django.utils import timezone

class TiposPessoa(models.Model):
    descricao = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Tipos de Pessoas"

    def __str__(self):
        return self.descricao

class Empresas(models.Model):
    razao_Social = models.TextField()
    identificacao = models.CharField(max_length=50)
    tipo_Pessoa = models.ForeignKey(TiposPessoa, on_delete=models.SET_NULL, null=True)
    cnpj = models.CharField(max_length=15)
    inscricao_Estadual = models.CharField(max_length=20)
    inscricao_Municipal = models.CharField(max_length=20)
    endereco = models.TextField()
    bairro = models.CharField(max_length=50)
    municipio = models.TextField()
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.TextField()
    email = models.TextField()
    nome_Titular = models.TextField()
    cpf = models.CharField(max_length=50)
    funcao = models.TextField()

    def __str__(self):
        return self.razaoSocial

    class Meta:
        verbose_name_plural = "Empresas"


class Clientes(models.Model):
    razao_Social = models.TextField()
    identificacao = models.CharField(max_length=50)
    classificacao = models.CharField(max_length=18)
    tipo_Pessoa = models.ForeignKey(TiposPessoa, on_delete=models.SET_NULL, null=True)
    cnpjCpf = models.CharField(max_length=15)
    inscricao_Estadual = models.CharField(max_length=20)
    inscricao_Municipal = models.CharField(max_length=20)
    endereco = models.TextField()
    bairro = models.CharField(max_length=50)
    municipio = models.TextField()
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.TextField()
    email = models.TextField()
    nome_Titular = models.TextField()
    funcao = models.TextField()

    def __str__(self):
        return self.razaoSocial+" - "+self.cnpjCpf

    class Meta:
        verbose_name_plural = "Clientes"


class Fornecedores(models.Model):
    razao_Social = models.TextField()
    identificacao = models.CharField(max_length=50)
    classificacao = models.CharField(max_length=18)
    tipo_Pessoa = models.ForeignKey(TiposPessoa, on_delete=models.SET_NULL, null=True)
    cnpjCpf = models.CharField(max_length=15)
    inscricao_Estadual = models.CharField(max_length=20)
    inscricao_Municipal = models.CharField(max_length=20)
    endereco = models.TextField()
    bairro = models.CharField(max_length=50)
    municipio = models.TextField()
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.TextField()
    email = models.TextField()
    nome_Titular = models.TextField()
    cpf = models.CharField(max_length=50)
    funcao = models.TextField()

    def __str__(self):
        return self.razaoSocial+" - "+self.cnpjCpf

    class Meta:
        verbose_name_plural = "Fornecedores"


class ContasBancarias(models.Model):
    classificacao = models.CharField(max_length=18)
    descricao = models.TextField()
    numeroConta = models.CharField(max_length=20)
    numero_Agencia = models.CharField(max_length=20)
    data_Saldo_Inicial = models.DateField(blank=False, null=False)
    saldo_Inicial = models.CharField(max_length=14)
    caixa = models.BooleanField(default=False)
    banco = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Contas Bancarias"


class PlanosDeContas(models.Model):
    Conta_Bancaria = models.ForeignKey(ContasBancarias, on_delete=models.PROTECT)
    classificacao = models.CharField(max_length=18)
    tipo_Conta = models.CharField(max_length=15)
    descricao = models.TextField()
    caixa = models.BooleanField(default=False)
    banco = models.BooleanField(default=False)
    cliente = models.BooleanField(default=False)
    fornecedor = models.BooleanField(default=False)
    entrada_Recurso = models.BooleanField(default=False)
    saida_Recurso = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Planos de Contas"


class LancamentosReceber(models.Model):
    Cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    Empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT)
    data_Vencimento = models.DateField(blank=False, null=False)
    data_Emissao = models.DateField(blank=False, null=False)
    valor_Titulo = models.CharField(max_length=14)
    numero_Documento = models.CharField(max_length=20)

    def __str__(self):
        return self.Cliente+" valor: "+self.valorTitulo

    class Meta:
        verbose_name_plural = "Lancamentos a Receber"


class FormasPagamento(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Formas de Pagamento"


class BaixasReceber(models.Model):
    Forma_Pagamento = models.ForeignKey(FormasPagamento, on_delete=models.PROTECT)
    Lancamento_Receber = models.ForeignKey(LancamentosReceber, on_delete=models.PROTECT)
    descricao = models.TextField()
    disponibilidade = models.CharField(max_length=12)
    dataBaixa = models.DateField(blank=True, null=True)
    valorPago = models.CharField(max_length=14)
    residual = models.CharField(max_length=14)

    def __str__(self):
        return self.valorPago

    class Meta:
        verbose_name_plural = "Baixas a Receber"


class BaixasPagar(models.Model):
    Forma_Pagamento = models.ForeignKey(FormasPagamento, on_delete=models.PROTECT)
    Lancamento_Receber = models.ForeignKey(LancamentosReceber, on_delete=models.PROTECT)
    descricao = models.TextField()
    disponibilidade = models.CharField(max_length=12)
    dataBaixa = models.DateField(blank=True, null=True)
    valorPago = models.CharField(max_length=14)
    residual = models.CharField(max_length=14)

    def __str__(self):
        return self.valorPago

    class Meta:
        verbose_name_plural = "Baixas a Pagar"

class LancamentosPagar(models.Model):
    Fornecedor = models.ForeignKey(Fornecedores, on_delete=models.PROTECT)
    Empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT)
    data_Vencimento = models.DateField(blank=False, null=False)
    data_Emissao = models.DateField(blank=False, null=False)
    valor_Titulo = models.TextField(max_length=14)
    numero_Documento = models.CharField(max_length=20)

    def __str__(self):
        return self.valorTitulo

    class Meta:
        verbose_name_plural = "Lancamentos a Pagar"


class Tesouraria(models.Model):
    Empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT)
    Cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    Plano_De_Contas = models.ForeignKey(PlanosDeContas, on_delete=models.PROTECT)
    Forma_Pagamento = models.ForeignKey(FormasPagamento, on_delete=models.PROTECT)
    Fornecedor = models.ForeignKey(Fornecedores, on_delete=models.PROTECT)
    valor = models.CharField(max_length=14)
    numero = models.CharField(max_length=15)
    data_Vencimento = models.DateField(blank=False, null=False)
    data_Emissao = models.DateField(blank=False, null=False)
    data_Disponibilidade = models.DateField(blank=False, null=False)

    class Meta:
        verbose_name_plural = "Tesourarias"