from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lancamento_receber_list', views.lancamento_receber_list, name='lancamento_receber_list'),
    path('lancamento_edit/<int:pk>/', views.lancamento_receber_edit, name='lancamento_receber_edit'),
    path('lancamento_edit', views.lancamento_receber_edit, name='lancamento_receber_edit'),
    path('delete_lancamento_receber/<int:pk>/', views.delete_lancamento_receber, name='delete_lancamento_receber'),
    path('relatorio_lancamentos_receber', views.relatorio_lancamentos_receber, name='relatorio_lancamentos_receber'),

]