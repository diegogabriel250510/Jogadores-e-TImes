from django.shortcuts import render,redirect
from .models import Time
from django.shortcuts import render, get_object_or_404
# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return  render(request, 'cadastro_time.html')
    elif request.method== 'POST':
        nome = request.POST.get('nome')
        titulos = request.POST.get('titulos')
        fundacao = request.POST.get('fundacao')
        
        # Crie um novo jogador e o salve no banco de dados
        time = Time(nome=nome, titulos=titulos, fundacao=fundacao)
        time.save()
        
        # Recupere todos os jogadores do banco de dados
        lista_times = Time.objects.all()
        
        return render(request, 'home_times.html', {'times': lista_times})
    
def visualizar(request, id):
    lista_times = Time.objects.all()
    time = Time.objects.filter(id=id)
    return render(request, 'visualizar_time.html', {'time':time})

def alterar(request, id):
    if request.method == 'GET':
        time_mudar = Time.objects.filter(id=id)
        return render(request, 'alterar_time.html', {'time_mudar':time_mudar})
    elif request.method == 'POST':
        lista_times = Time.objects.all()
        nome = request.POST.get('nome')
        titulos = request.POST.get('titulos')
        fundacao = request.POST.get('fundacao')
        time_mudar = Time.objects.get(id=id)
        time_mudar.nome = nome
        time_mudar.titulos = titulos
        time_mudar.fundacao = fundacao
        time_mudar.save()
        return render(request, 'home_times.html', {'times':lista_times})

def deletar(request, id):
    lista_times = Time.objects.all()
    time = Time.objects.filter(id=id)
    time.delete()
    return render(request, 'home_times.html', {'times':lista_times})

def home(request):
    return render(request, 'home_times.html')

