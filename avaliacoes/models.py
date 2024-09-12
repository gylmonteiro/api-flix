from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from filmes.models import Filme


# Create your models here.
class Avaliacao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.PROTECT, related_name='avaliacoes')
    estrelas = models.IntegerField(validators=[MinValueValidator(0, 'Não pode enviar um valor menor que 0'), MaxValueValidator(5, 'Não pode enviar um valor maior que 5')])
    comentario = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.filme}: {self.estrelas}"