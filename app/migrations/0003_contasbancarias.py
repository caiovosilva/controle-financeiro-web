# Generated by Django 2.0.8 on 2018-09-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_fornecedores'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContasBancarias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classificacao', models.CharField(max_length=18)),
                ('descricao', models.TextField()),
                ('numeroConta', models.CharField(max_length=20)),
                ('numeroAgencia', models.CharField(max_length=20)),
                ('dataSaldoInicial', models.DateField()),
                ('saldoInicial', models.CharField(max_length=14)),
                ('caixa', models.CharField(max_length=1)),
                ('banco', models.CharField(max_length=1)),
            ],
        ),
    ]
