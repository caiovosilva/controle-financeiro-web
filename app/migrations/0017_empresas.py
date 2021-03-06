# Generated by Django 2.0.8 on 2018-10-09 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_tipospessoa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_Social', models.TextField()),
                ('identificacao', models.CharField(max_length=50)),
                ('cnpj', models.CharField(max_length=15)),
                ('inscricao_Estadual', models.CharField(max_length=20)),
                ('inscricao_Municipal', models.CharField(max_length=20)),
                ('endereco', models.TextField()),
                ('bairro', models.CharField(max_length=50)),
                ('municipio', models.TextField()),
                ('cep', models.CharField(max_length=10)),
                ('uf', models.CharField(max_length=2)),
                ('telefone', models.TextField()),
                ('email', models.TextField()),
                ('nome_Titular', models.TextField()),
                ('cpf', models.CharField(max_length=50)),
                ('funcao', models.TextField()),
                ('tipo_Pessoa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.TiposPessoa')),
            ],
            options={
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]
