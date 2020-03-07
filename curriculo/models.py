from django.db import models

class Sobre(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, null=True, blank=True)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    cep = models.IntegerField()
    telefone = models.CharField(max_length=9)
    ddd = models.IntegerField()
    email = models.CharField(max_length=100)
    sobre_mim = models.TextField()
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    github = models.CharField(max_length=100, null=True, blank=True)
    nacionalidade = models.CharField(max_length=100, null=True, blank=True)
    estado_civil = models.CharField(max_length=100, null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='foto_perfil')

    def __str__(self):
        return self.nome


class Experiencia(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    inicio = models.DateField(null=True, blank=True)
    fim = models.DateField(null=True, blank=True)
    atual = models.BooleanField()
    descricao = models.TextField()

    def __str__(self):
        return self.cargo


class Escolaridade(models.Model):
    curso = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    grau = models.CharField(max_length=100)
    inicio = models.DateField(null=True, blank=True)
    fim = models.DateField(null=True, blank=True)
    nota = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.curso


class Skill(models.Model):
    TIPO_CHOICES = (
            (1, "Linguagem"),
            (2, "Framework"),
            (3, "Ferramenta"),
            (4, "Outra Tecnologia"),
            (5, "workflow")
        )
    skill = models.CharField(max_length=100)
    tipo = models.IntegerField(choices= TIPO_CHOICES, default=1)
    web_icon = models.CharField(max_length=100, null=True, blank=True)
    icone = models.ImageField(upload_to='icones_tecnologias', null=True, blank=True)

    def __str__(self):
        return self.skill
    

class Objetivo(models.Model):
    objetivo = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.objetivo


class Curso(models.Model):
    curso = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100, null=True, blank=True)
    horas = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.curso


class Complementar(models.Model):
    informacao = models.CharField(max_length=100)

    def __str__(self):
        return self.informacao