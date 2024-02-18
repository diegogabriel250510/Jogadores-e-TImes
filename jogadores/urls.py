from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('cadastrar/', views.cadastrar, name='cadastrar_jogador'),
    path('visualizar/<int:id>', views.visualizar, name='visualizar_jogador'),
    path('alterar/<int:id>/', views.alterar, name='alterar_jogador'),
    path('deletar/<int:id>/', views.deletar, name='deletar_jogador')
]
