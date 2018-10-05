# Generated by Django 2.0.8 on 2018-10-03 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_tesouraria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baixaspagar',
            options={'verbose_name_plural': 'BaixasPagar'},
        ),
        migrations.AlterModelOptions(
            name='baixasreceber',
            options={'verbose_name_plural': 'BaixasReceber'},
        ),
        migrations.AlterModelOptions(
            name='clientes',
            options={'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='contasbancarias',
            options={'verbose_name_plural': 'ContasBancarias'},
        ),
        migrations.AlterModelOptions(
            name='empresas',
            options={'verbose_name_plural': 'Empresas'},
        ),
        migrations.AlterModelOptions(
            name='formaspagamento',
            options={'verbose_name_plural': 'FormasPagamento'},
        ),
        migrations.AlterModelOptions(
            name='fornecedores',
            options={'verbose_name_plural': 'Fornecedores'},
        ),
        migrations.AlterModelOptions(
            name='lancamentospagar',
            options={'verbose_name_plural': 'LancamentosPagar'},
        ),
        migrations.AlterModelOptions(
            name='lancamentosreceber',
            options={'verbose_name_plural': 'LancamentosReceber'},
        ),
        migrations.AlterModelOptions(
            name='planosdecontas',
            options={'verbose_name_plural': 'PlanosDeContas'},
        ),
        migrations.AlterModelOptions(
            name='tesouraria',
            options={'verbose_name_plural': 'Tesourarias'},
        ),
        migrations.RemoveField(
            model_name='clientes',
            name='cpf',
        ),
    ]
