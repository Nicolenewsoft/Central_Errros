# Generated by Django 3.0.3 on 2020-07-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_auto_20200702_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
