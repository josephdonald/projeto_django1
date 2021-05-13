from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    quantidade = models.IntegerField('Quantidade')

    def __str__(self):
        return "{}".format(self.nome)
        # return f'{self.nome}' + 'Quantidade:'+{self.quantidade}


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return "{} {}".format(self.nome, self.sobrenome)
