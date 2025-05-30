from django.db import models
from django.utils import timezone

class Item(models.Model):
    nome = models.CharField(max_length=100)
    codigo_referencia = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)
    localizacao = models.CharField(max_length=50, help_text="Localização na prateleira/armário")
    quantidade_atual = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo_referencia})"

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"
        ordering = ['nome']

class MovimentacaoEstoque(models.Model):
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SAIDA', 'Saída'),
    ]

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='movimentacoes')
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    quantidade = models.IntegerField()
    data_movimentacao = models.DateTimeField(default=timezone.now)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.item.nome} ({self.quantidade})"

    class Meta:
        verbose_name = "Movimentação de Estoque"
        verbose_name_plural = "Movimentações de Estoque"
        ordering = ['-data_movimentacao']
