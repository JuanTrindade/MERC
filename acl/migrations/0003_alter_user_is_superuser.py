# Generated by Django 5.1.3 on 2024-11-13 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acl', '0002_useersupplier_userclient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(verbose_name='É Admin?'),
        ),
    ]
