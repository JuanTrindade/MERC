# Generated by Django 5.1.3 on 2024-11-19 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_alter_product_dt_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dt_joined',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de Entrada'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_choices',
            field=models.DateTimeField(choices=[('AL', 'Alimentos'), ('EL', 'Eletrônicos'), ('FE', 'Ferramentas'), ('VE', 'Vestimentas')], max_length=2, verbose_name='Categoria do Proudto'),
        ),
    ]
