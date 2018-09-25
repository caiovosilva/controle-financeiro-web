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

    # created_date = models.DateTimeField(
    #         default=timezone.now)
    # published_date = models.DateTimeField(
    #         blank=True, null=True)

    def save(self):
        self.save()

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

    def save(self):
        self.save()

    def __str__(self):
        return self.razaoSocial+" - "+self.cnpjCpf