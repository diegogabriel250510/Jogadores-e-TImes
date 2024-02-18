from django.shortcuts import render,redirect
from .models import Jogador
def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        posicao = request.POST.get('posicao')
        idade = request.POST.get('idade')
        
        # Crie um novo jogador e o salve no banco de dados
        jogador = Jogador(nome=nome, posicao=posicao, idade=idade)
        jogador.save()
        
        # Recupere todos os jogadores do banco de dados
        lista_jogadores = Jogador.objects.all()
        
        return render(request, 'home_jogador.html', {'jogadores': lista_jogadores})

def visualizar(request, id):
    lista_jogadores = Jogador.objects.filter(id=id)
    return render(request, 'visualizar_jogador.html', {'jogadores': lista_jogadores})

def alterar(request, id):
    if request.method == 'GET':
        jogador_mudar = Jogador.objects.filter(id=id)
        return render(request, 'alterar.html', {'jogador_mudar':jogador_mudar})
    elif request.method == 'POST':
        lista_jogadores = Jogador.objects.all()
        nome = request.POST.get('nome')
        posicao = request.POST.get('posicao')
        idade = request.POST.get('idade')
        jogador_mudar = Jogador.objects.get(id=id)
        jogador_mudar.nome = nome
        jogador_mudar.idade = idade
        jogador_mudar.posicao = posicao
        jogador_mudar.save()
        return render(request, 'home_jogador.html', {'jogadores':lista_jogadores})
        
def deletar(request, id):
    lista_jogadores = Jogador.objects.all()
    jogador = Jogador.objects.filter(id=id)
    jogador.delete()
    return render(request, 'home_jogador.html', {'jogadores':lista_jogadores})
    
def home(request):
    return render(request, 'home_jogador.html')
