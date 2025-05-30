from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item, MovimentacaoEstoque
from django.db.models import F

# Create your views here.

class DashboardView(ListView):
    model = Item
    template_name = 'estoque/dashboard.html'
    context_object_name = 'itens'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itens_baixo_estoque'] = Item.objects.filter(
            quantidade_atual__lte=F('estoque_minimo')
        )
        return context

class ItemCreateView(CreateView):
    model = Item
    template_name = 'estoque/item_form.html'
    fields = ['nome', 'codigo_referencia', 'descricao', 'localizacao', 
              'quantidade_atual', 'estoque_minimo', 'preco_unitario']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        messages.success(self.request, 'Item cadastrado com sucesso!')
        return super().form_valid(form)

class ItemUpdateView(UpdateView):
    model = Item
    template_name = 'estoque/item_form.html'
    fields = ['nome', 'codigo_referencia', 'descricao', 'localizacao', 
              'quantidade_atual', 'estoque_minimo', 'preco_unitario']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        messages.success(self.request, 'Item atualizado com sucesso!')
        return super().form_valid(form)

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'estoque/item_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Item excluído com sucesso!')
        return super().delete(request, *args, **kwargs)

class MovimentacaoEstoqueView(CreateView):
    model = MovimentacaoEstoque
    template_name = 'estoque/movimentacao_form.html'
    fields = ['item', 'tipo', 'quantidade', 'observacao']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        movimentacao = form.save(commit=False)
        item = movimentacao.item
        
        if movimentacao.tipo == 'ENTRADA':
            item.quantidade_atual += movimentacao.quantidade
        else:  # SAIDA
            if item.quantidade_atual < movimentacao.quantidade:
                messages.error(self.request, 'Quantidade insuficiente em estoque!')
                return self.form_invalid(form)
            item.quantidade_atual -= movimentacao.quantidade
        
        item.save()
        messages.success(self.request, 'Movimentação registrada com sucesso!')
        return super().form_valid(form)
