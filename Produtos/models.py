from django.db import models
from datetime import datetime

class Pipeline(models.Model):

    EMPRESAS = (
        ('EQUIPE', 'EQUIPE'),
        ('FCB', 'FCB'),
        ('GALERIA','GALERIA'),
        ('DPZT', 'DPZT')
    )
    nome_pipeline = models.CharField(unique=True, max_length=200)
    empresa = models.CharField(max_length=50, choices=EMPRESAS, blank=False, null=True)
    redesocal = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(default=datetime.now, blank=True)
    status = models.BooleanField() 


    def __str__(self):
        return self.nome_pipeline
