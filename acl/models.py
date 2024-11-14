from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    is_superuser = models.BooleanField(verbose_name='Admin', help_text='Designado para usuários Admins')
    first_name = models.CharField(verbose_name='Nome', max_length=150, blank=False)
    last_name = models.CharField(verbose_name='Sobrenome', max_length=150, blank=False)
    email = models.EmailField(verbose_name='E-mail', blank=False)
    password = models.CharField(verbose_name='Senha', max_length=150, blank=False)
    
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