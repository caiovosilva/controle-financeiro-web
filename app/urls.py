from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.lancamento_receber_list, name='lancamento_receber_list'),
    path('lancamento_edit/<int:pk>/', views.lancamento_receber_edit, name='lancamento_receber_edit'),

]