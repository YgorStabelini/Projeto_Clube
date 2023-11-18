from django.db import models

class EspacoLocavel(models.Model):
    nome = models.CharField(max_length=100)
    tamanho = models.DecimalField(max_digits=5, decimal_places=2)
    capacidade_pessoas = models.PositiveIntegerField()
    data_construcao_aquisicao = models.DateField()
    locavel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome