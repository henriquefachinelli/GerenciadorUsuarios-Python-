from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    EMPRESAS = (
        ('EQUIPE', 'EQUIPE'),
        ('FCB', 'FCB'),
        ('GALERIA','GALERIA'),
        ('DPZT', 'DPZT')
    )
    grupo = models.CharField(max_length=50, choices=EMPRESAS, blank=False, null=True)

    def __str__(self):
        return self.username