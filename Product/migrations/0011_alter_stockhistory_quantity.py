# Generated by Django 5.1.3 on 2024-11-20 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0010_alter_stockhistory_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhistory',
            name='quantity',
            field=models.FloatField(verbose_name='Quantidade'),
        ),
    ]
