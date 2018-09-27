# Generated by Django 2.0.8 on 2018-09-27 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contasbancarias'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaixasPagar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('disponibilidade', models.CharField(max_length=12)),
                ('dataBaixa', models.DateField(blank=True, null=True)),
                ('valorPago', models.CharField(max_length=14)),
                ('residual', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='BaixasReceber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('disponibilidade', models.CharField(max_length=12)),
                ('dataBaixa', models.DateField(blank=True, null=True)),
                ('valorPago', models.CharField(max_length=14)),
                ('residual', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='FormasPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LancamentosReceber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataVencimento', models.DateField()),
                ('dataEmissao', models.DateField()),
                ('valorTitulo', models.CharField(max_length=14)),
                ('numeroDocumento', models.CharField(max_length=20)),
                ('Cliente_Id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Clientes')),
                ('Empresa_Id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Empresas')),
            ],
        ),
        migrations.CreateModel(
            name='PlanosDeContas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classificacao', models.CharField(max_length=18)),
                ('tipoConta', models.CharField(max_length=15)),
                ('descricao', models.TextField()),
                ('caixa', models.CharField(max_length=1)),
                ('banco', models.CharField(max_length=1)),
                ('cliente', models.CharField(max_length=1)),
                ('fornecedor', models.CharField(max_length=1)),
                ('entradaRecurso', models.CharField(max_length=1)),
                ('saidaRecurso', models.CharField(max_length=1)),
                ('ContaBancaria_Id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.ContasBancarias')),
            ],
        ),
        migrations.AddField(
            model_name='baixasreceber',
            name='FormaPagamento_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.FormasPagamento'),
        ),
        migrations.AddField(
            model_name='baixasreceber',
            name='LancamentoReceber_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.LancamentosReceber'),
        ),
        migrations.AddField(
            model_name='baixaspagar',
            name='FormaPagamento_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.FormasPagamento'),
        ),
        migrations.AddField(
            model_name='baixaspagar',
            name='LancamentoReceber_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.LancamentosReceber'),
        ),
    ]
