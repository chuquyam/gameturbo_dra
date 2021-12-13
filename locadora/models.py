from django.db import models

#Classe para Base de Dados do Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=80, verbose_name="Nome")
    CPF = models.CharField(max_length=20)
    email = models.EmailField(max_length=20,verbose_name="E-mail")
    telefone = models.CharField(max_length=20)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

#Classe para Base de Dados do Jogo
class Jogo(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Título")
    tipo = models.CharField(max_length=10)
    fabricante = models.CharField(max_length=40)
    plataforma = models.CharField(max_length=40)
    faixaetaria = models.IntegerField(verbose_name="Faixa Etária")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    preco = models.FloatField(verbose_name="Preço")

    def __str__(self):
        return self.titulo
        #poderia usar formatando
        #return "{} ({})".format(self.titulo, self.plataforma)

#Classe para Base de Dados da operação de aluguel de jogos
class Alugar(models.Model):
    data_aluguel = models.DateField()
    data_devolucao = models.DateField()
    codigo_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    codigo_jogo = models.ForeignKey(Jogo, on_delete=models.PROTECT)
    quantidade = models.IntegerField(verbose_name="Quantidade")
    total = models.FloatField(verbose_name="Total a pagar")

    def __str__(self):
        return "{} ({})".format(self.codigo_cliente, self.codigo_jogo)