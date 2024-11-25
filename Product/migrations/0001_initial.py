# Generated by Django 5.1.3 on 2024-11-19 02:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=120, verbose_name='Nome do Produto')),
                ('price', models.FloatField(max_length=120, verbose_name='Preço')),
                ('product_choices', models.CharField(choices=[('AL', 'Alimentos'), ('EL', 'Eletrônicos'), ('FE', 'Ferramentas'), ('VE', 'Vestimentas')], max_length=2, verbose_name='Categoria do Proudto')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
            ],
        ),
    ]