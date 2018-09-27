from django.db import models
from django.utils import timezone


class Empresas(models.Model):
    razaoSocial = models.TextField()
    identificacao = models.CharField(max_length=50)
    tipoPessoa = models.CharField(max_length=10)
    cnpj = models.CharField(max_length=15)
    inscricaoEstadual = models.CharField(max_length=20)
    inscricaoMunicipal = models.CharField(max_length=20)
    endereco = models.TextField()
    bairro = models.CharField(max_length=50)
    municipio = models.TextField()
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.TextField()
    email = models.TextField()
    nomeTitular = models.TextField()
    cpf = models.CharField(max_length=50)
    funcao = models.TextField()

    # def save(self):
    #     self.save()

    def __str__(self):
        return self.razaoSocial


class Clientes(models.Model):
    razaoSocial = models.TextField()
    identificacao = models.CharField(max_length=50)
    classificacao = models.CharField(max_length=18)
    tipoPessoa = models.CharField(max_length=10)
    cnpjCpf = models.CharField(max_length=15)
    inscricaoEstadual = models.CharField(max_length=20)
    inscricaoMunicipal = models.CharField(max_length=20)
    endereco = models.TextField()
    bairro = models.CharField(max_length=50)
    municipio = models.TextField()
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.TextField()
    email = models.TextField()
    nomeTitular = models.TextField()
    cpf = models.CharField(max_length=50)
    funcao = models.TextField()

    def __str__(self):
        return self.razaoSocial+" - "+self.cnpjCpf


class Fornecedores(models.Model):
    razaoSocial = models.TextField()
    identificacao = models.CharField(max_length=50)
    classificacao = models.CharField(max_length=18)
    tipoPessoa = models.CharField(max_length=10)
    cnpjCpf = models.CharField(max_length=15)
    inscricaoEstadual = models.CharField(max_length=20)
    inscricaoMunicipal = models.CharField(max_length=20)
    endereco = models.TextField()
    bairro = models.CharField(max_length=50)
    municipio = models.TextField()
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.TextField()
    email = models.TextField()
    nomeTitular = models.TextField()
    cpf = models.CharField(max_length=50)
    funcao = models.TextField()

    def __str__(self):
        return self.razaoSocial+" - "+self.cnpjCpf


class ContasBancarias(models.Model):
    classificacao = models.CharField(max_length=18)
    descricao = models.TextField()
    numeroConta = models.CharField(max_length=20)
    numeroAgencia = models.CharField(max_length=20)
    dataSaldoInicial = models.DateField(blank=False, null=False)
    saldoInicial = models.CharField(max_length=14)
    caixa = models.CharField(max_length=1)
    banco = models.CharField(max_length=1)

    def __str__(self):
        return self.descricao


class PlanosDeContas(models.Model):
    ContaBancaria_Id = models.ForeignKey(ContasBancarias, on_delete=models.PROTECT)
    classificacao = models.CharField(max_length=18)
    tipoConta = models.CharField(max_length=15)
    descricao = models.TextField()
    caixa = models.CharField(max_length=1)
    banco = models.CharField(max_length=1)
    cliente = models.CharField(max_length=1)
    fornecedor = models.CharField(max_length=1)
    entradaRecurso = models.CharField(max_length=1)
    saidaRecurso = models.CharField(max_length=1)

    def __str__(self):
        return self.descricao


class LancamentosReceber(models.Model):
    Cliente_Id = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    Empresa_Id = models.ForeignKey(Empresas, on_delete=models.PROTECT)
    dataVencimento = models.DateField(blank=False, null=False)
    dataEmissao = models.DateField(blank=False, null=False)
    valorTitulo = models.CharField(max_length=14)
    numeroDocumento = models.CharField(max_length=20)

    def __str__(self):
        return self.Cliente_Id+" valor: "+self.valorTitulo


class FormasPagamento(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao


class BaixasReceber(models.Model):
    FormaPagamento_Id = models.ForeignKey(FormasPagamento, on_delete=models.PROTECT)
    LancamentoReceber_Id = models.ForeignKey(LancamentosReceber, on_delete=models.PROTECT)
    descricao = models.TextField()
    disponibilidade = models.CharField(max_length=12)
    dataBaixa = models.DateField(blank=True, null=True)
    valorPago = models.CharField(max_length=14)
    residual = models.CharField(max_length=14)

    def __str__(self):
        return self.valorPago


class BaixasPagar(models.Model):
    FormaPagamento_Id = models.ForeignKey(FormasPagamento, on_delete=models.PROTECT)
    LancamentoReceber_Id = models.ForeignKey(LancamentosReceber, on_delete=models.PROTECT)
    descricao = models.TextField()
    disponibilidade = models.CharField(max_length=12)
    dataBaixa = models.DateField(blank=True, null=True)
    valorPago = models.CharField(max_length=14)
    residual = models.CharField(max_length=14)

    def __str__(self):
        return self.valorPago


class LancamentosPagar(models.Model):
    Fornecedor_Id = models.ForeignKey(Fornecedores, on_delete=models.PROTECT)
    Empresa_Id = models.ForeignKey(Empresas, on_delete=models.PROTECT)
    dataVencimento = models.DateField(blank=False, null=False)
    dataEmissao = models.DateField(blank=False, null=False)
    valorTitulo = models.TextField(max_length=14)
    numeroDocumento = models.CharField(max_length=20)

    def __str__(self):
        return self.valorTitulo


class Tesouraria(models.Model):
    Empresa_Id = models.ForeignKey(Empresas, on_delete=models.PROTECT)
    Cliente_Id = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    PlanoDeContas_Id = models.ForeignKey(PlanosDeContas, on_delete=models.PROTECT)
    FormaPagamento_Id = models.ForeignKey(FormasPagamento, on_delete=models.PROTECT)
    Fornecedor_Id = models.ForeignKey(Fornecedores, on_delete=models.PROTECT)
    valor = models.CharField(max_length=14)
    numero = models.CharField(max_length=15)
    dataVencimento = models.DateField(blank=False, null=False)
    dataEmissao = models.DateField(blank=False, null=False)
    dataDisponibilidade = models.DateField(blank=False, null=False)