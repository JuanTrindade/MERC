from django.db import models

# Create your models here.
class JustATestModel(models.Model):
    testing = models.CharField(max_length=120)