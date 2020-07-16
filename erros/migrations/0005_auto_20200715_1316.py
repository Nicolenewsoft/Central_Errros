# Generated by Django 3.0.3 on 2020-07-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erros', '0004_auto_20200714_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='erros',
            options={'verbose_name': 'Erro', 'verbose_name_plural': 'Erros'},
        ),
        migrations.AddField(
            model_name='erros',
            name='arquiva',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='erros',
            name='categoria',
            field=models.CharField(choices=[('1', 'Produção'), ('2', 'Homologação'), ('3', 'Desenvolvimento')], max_length=1, verbose_name='Categoria'),
        ),
    ]