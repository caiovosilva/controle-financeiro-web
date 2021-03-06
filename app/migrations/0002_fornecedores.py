# Generated by Django 2.0.8 on 2018-09-25 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razaoSocial', models.TextField()),
                ('identificacao', models.CharField(max_length=50)),
                ('classificacao', models.CharField(max_length=18)),
                ('tipoPessoa', models.CharField(max_length=10)),
                ('cnpjCpf', models.CharField(max_length=15)),
                ('inscricaoEstadual', models.CharField(max_length=20)),
                ('inscricaoMunicipal', models.CharField(max_length=20)),
                ('endereco', models.TextField()),
                ('bairro', models.CharField(max_length=50)),
                ('municipio', models.TextField()),
                ('cep', models.CharField(max_length=10)),
                ('uf', models.CharField(max_length=2)),
                ('telefone', models.TextField()),
                ('email', models.TextField()),
                ('nomeTitular', models.TextField()),
                ('cpf', models.CharField(max_length=50)),
                ('funcao', models.TextField()),
            ],
        ),
    ]
