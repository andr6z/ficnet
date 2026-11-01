from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente

class Perfil(models.Model):
    SETOR_CHOICES = [
        ('ADMIN', 'Administrador-geral'),
        ('COMERCIAL', 'Funcionario - Comercial'),
        ('FINANCEIRO', 'Funcionário - Financeiro'),
        ('SUPORTE', 'Funcionário - Suporte Técnico'),
        ('CLIENTE', 'Cliente / Assinante'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    setor = models.CharField(max_length=20, choices=SETOR_CHOICES, default='CLIENTE', verbose_name="Perfil / Setor")
    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Cadastro de Cliente Vinculado"
    )

    def __str__(self):
        return f"{self.usuario.username} - {self.get_setor_display()}"
# Create your models here.
