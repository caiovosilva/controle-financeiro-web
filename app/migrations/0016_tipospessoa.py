# Generated by Django 2.0.8 on 2018-10-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0015_auto_20181009_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiposPessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Pessoas',
            },
        ),
    ]
