from django.db import models

class Dependente(models.Model):
    VINCULO_CHOICES = [
        ('pai', 'Pai'),
        ('mae', 'Mãe'),
        ('filho', 'Filho'),
        ('filha', 'Filha'),
        ('neto', 'Neto'),
    ]

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField()
    tipo_vinculo = models.CharField(max_length=20, choices=VINCULO_CHOICES)
    socio_titular = models.ForeignKey('Associado', on_delete=models.CASCADE, related_name='dependentes_associado')

    def __str__(self):
        return self.nome

class Associado(models.Model):
    TIPO_ASSOCIACAO_CHOICES = [
        ('fundador', 'Sócio Fundador'),
        ('proprietario', 'Sócio Proprietário'),
        ('cotista', 'Sócio Cotista'),
        ('voluntario', 'Sócio Voluntário'),
    ]

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField()
    tipo_associacao = models.CharField(max_length=20, choices=TIPO_ASSOCIACAO_CHOICES)
    dependentes = models.ManyToManyField(Dependente, blank=True, related_name='associados_dependente')

    def __str__(self):
        return self.nome
