# Generated by Django 2.0.8 on 2018-10-03 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20181003_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='tipoPessoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.TiposPessoa'),
        ),
        migrations.AddField(
            model_name='empresas',
            name='tipoPessoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.TiposPessoa'),
        ),
        migrations.AddField(
            model_name='fornecedores',
            name='tipoPessoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.TiposPessoa'),
        ),
    ]