from django.db import models
from django.urls import reverse

# Create your models here.

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "pessoa"
        verbose_name_plural = "pessoas"

    def __str__(self):
        return self.nome_completo

    def get_absolute_url(self):
        return reverse("pessoa_detail", kwargs={"pk": self.pk})

class Contato(models.Model):
    #esse modelo é usado para criar um relacionamento entre Pessoa e Contato
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)#pessoa a qual será vinculada o contato
    tipo = models.CharField(max_length=1, choices=(('R', 'Residencial'), ('C', 'Comercial'), ('F', 'Fax'), ('E', 'E-mail'), ('M', 'Celular')))
    contato = models.CharField(max_length=256)

    class Meta:
        verbose_name = "contato"
        verbose_name_plural = "contatos"

    def __str__(self):
        return self.contato
