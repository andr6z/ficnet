from django.db import models

# Create your models here.
class Plano(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Plano")
    velocidade = models.IntegerField(verbose_name="Velocidade (Mbps)")
    descricao = models.TextField(blank=True, verbose_name="Benefícios do Plano")
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True, verbose_name="Disponível para venda")
    
    def __str__ (self):
        return self.nome