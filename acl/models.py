from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    pass

# 
# 
class UserClient(models.Model):
    cpf = models.CharField(
        max_length=120,
        null=False,
        blank=False,
        primary_key=True,
        verbose_name='CPF'
    )

    client_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Nome'
    )

    cellphone = models.FloatField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name='Telefone'
    )

    address = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Endereço'
    )

    email = models.CharField(
        max_length=120,
        null=False,
        blank=False,
        verbose_name='E-mail'
    )

# 
# 
class UseerSupplier(models.Model):
    CATEGORY_SUPPLIER_CHOICES = {
        'EL': 'Eletrônicos',
        'AL': 'Alimentos',
        'FE': 'Ferramentas',
        'RO': 'Roupas'
    }

    cnpj = models.CharField(
        max_length=120,
        null=False,
        blank=False,
        primary_key=True,
        verbose_name='CNPJ'
    )

    supplier_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Nome'
    )

    cellphone = models.FloatField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name='Telefone'
    )

    address = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Endereço'
    )

    email = models.CharField(
        max_length=120,
        null=False,
        blank=False,
        verbose_name='E-mail'
    )

    supplier_category = models.CharField(max_length=2, choices=CATEGORY_SUPPLIER_CHOICES)