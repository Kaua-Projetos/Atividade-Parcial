from django.contrib import admin
from .models import Item, MovimentacaoEstoque

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo_referencia', 'quantidade_atual', 'estoque_minimo', 'localizacao', 'preco_unitario')
    list_filter = ('localizacao',)
    search_fields = ('nome', 'codigo_referencia')
    ordering = ('nome',)

@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoqueAdmin(admin.ModelAdmin):
    list_display = ('item', 'tipo', 'quantidade', 'data_movimentacao')
    list_filter = ('tipo', 'data_movimentacao')
    search_fields = ('item__nome', 'observacao')
    ordering = ('-data_movimentacao',)
