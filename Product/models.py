from django.db import models


class Product(models.Model):    
    CATEGORY_PRODUCT_CHOICES = {
        'AL': 'Alimentos',
        'EL': 'Eletrônicos',
        'FE': 'Ferramentas',
        'VE': 'Vestimentas'
    }
    
    name = models.CharField(
        max_length=120,
        null=False,
        blank=False,
        verbose_name='Nome do Produto'
    )

    price = models.FloatField(
        max_length=120,
        null=False,
        blank=False,
        verbose_name='Preço'
    )

    product_choices = models.CharField(
        max_length=2,
        choices=CATEGORY_PRODUCT_CHOICES,
        null=False,
        blank=False,
        verbose_name='Categoria do Produto'
    )

    def __str__(self):
        return f'{self.name}'


class StockHistory(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='stock'
    )

    quantity = models.FloatField(
        null=False, 
        blank=False,
        verbose_name='Quantidade'
    )

    entered_at = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Entrada'
    )

    leaved_at = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Saida'
    )


class ProductSummary(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        null=False
    )

    summary = models.CharField(
        max_length=255,
        null=False
    )