from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    codigo_referencia = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)
    localizacao = models.CharField(max_length=100)
    quantidade_atual = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=0)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class MovimentacaoEstoque(models.Model):
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SAIDA', 'Saída'),
    ]

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    quantidade = models.IntegerField()
    observacao = models.TextField(blank=True)
    data_movimentacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.item.nome} ({self.quantidade})"
