# Generated by Django 5.1.3 on 2024-11-25 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0011_alter_stockhistory_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhistory',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='Product.product'),
        ),
    ]