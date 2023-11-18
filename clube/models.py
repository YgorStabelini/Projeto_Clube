from django.db import models

class Convidado(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20)
    celular = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Evento(models.Model):
    espaco_locavel = models.ForeignKey('EspacoLocavel', on_delete=models.CASCADE)
    convidados = models.ManyToManyField(Convidado)
    valor_locacao = models.DecimalField(max_digits=10, decimal_places=2)
    data_inicio = models.DateField()
    hora_inicio = models.TimeField()
    data_fim = models.DateField()
    hora_fim = models.TimeField()
    responsavel_locacao = models.ForeignKey('Associado', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.espaco_locavel} - {self.data_inicio}"
