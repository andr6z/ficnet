from django.db import models
class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    sobrenome = models.CharField(max_length=200, verbose_name="Sobrenome")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    email = models.EmailField(unique=True, verbose_name="E-mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone/WhatsApp")
    endereco = models.CharField(max_length=255, verbose_name="Endereço de Instalação")
    ativo = models.BooleanField(default=True, verbose_name="Cadastro Ativo")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    def __str__(self):
        return f"{self.nome} ({self.cpf})"