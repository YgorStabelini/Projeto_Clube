from django.db import models

class Fornecedor(models.Model):
    nome_razao_social = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    facebook = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    contato = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_razao_social