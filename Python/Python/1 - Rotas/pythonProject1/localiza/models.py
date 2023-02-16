from django.db import models

# Create your models here.


class resposta2(models.Model):
    bairro = models.CharField(max_length=50, default='default_value')
    rua = models.CharField(max_length=50)
    regiao = models.CharField(max_length=50)

    def __str__(self):
        return self.bairro
