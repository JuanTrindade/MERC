from django.db import models


class Product(models.Model):
    CATEGORY_PRODUCT_CHOICES = {
        'AL': 'Alimento',
        'EL': 'Eletrônico',
        'FE': 'Ferramentas',
        'VE': 'Vestimentas'
    }
    
    product_name = models.CharField(
        max_length=120,
        null=False,
        blank=False,
    )

    price = models.FloatField(
        max_length=120,
        null=False,
        blank=False
    )

    product_choices = models.CharField(
        max_length=2,
        choices=CATEGORY_PRODUCT_CHOICES,
        null=False,
        blank=False
    )

