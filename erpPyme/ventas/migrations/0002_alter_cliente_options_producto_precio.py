# Generated by Django 4.0.6 on 2024-01-09 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'cliente', 'verbose_name_plural': 'clientes'},
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
