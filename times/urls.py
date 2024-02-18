from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('cadastrar/', views.cadastro, name='cadastrar_time'),
    path('visualizar/<int:id>', views.visualizar, name='visualizar_time'),
    path('alterar/<int:id>/', views.alterar, name='alterar_time'),
    path('deletar/<int:id>/', views.deletar, name='deletar_time')
]
