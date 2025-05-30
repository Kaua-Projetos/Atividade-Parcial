from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('item/novo/', views.ItemCreateView.as_view(), name='item_create'),
    path('item/<int:pk>/editar/', views.ItemUpdateView.as_view(), name='item_update'),
    path('item/<int:pk>/excluir/', views.ItemDeleteView.as_view(), name='item_delete'),
    path('movimentacao/nova/', views.MovimentacaoEstoqueView.as_view(), name='movimentacao_create'),
] 