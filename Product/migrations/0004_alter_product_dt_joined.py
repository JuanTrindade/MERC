# Generated by Django 5.1.3 on 2024-11-19 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_product_dt_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dt_joined',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Entrada'),
        ),
    ]
