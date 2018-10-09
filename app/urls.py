from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.ver_lancamento_contas_receber, name='ver_lancamento_contas_receber'),
]