# Generated by Django 5.1.3 on 2024-11-19 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_alter_stock_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dt_joined',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de Entrada'),
        ),
    ]