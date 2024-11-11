from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    pass
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # phone_number = models.FloatField(max_length=120, null=True, blank=True)
    # username = models.CharField(
    #     max_length=120,
    #     verbose_name='Nome de Usuário',
    #     null=False,
    #     blank=False
        
    # )

    # password = models.CharField(
    #     max_length=120,
    #     verbose_name='Senha',
    #     null=False,
    #     blank=False

    # )

    # email = models.CharField(
    #     max_length=120,
    #     verbose_name='E-mail',
    #     null=False,
    #     blank=False

    # )