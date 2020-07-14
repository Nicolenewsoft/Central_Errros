# Generated by Django 3.0.3 on 2020-07-14 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erros', '0002_auto_20200714_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erros',
            name='categoria',
            field=models.ForeignKey(choices=[('p', 'Produção'), ('h', 'Homologação'), ('d', 'Desenvolvimento'), ('a', 'Arquivado')], on_delete=django.db.models.deletion.CASCADE, to='erros.Categoria'),
        ),
    ]