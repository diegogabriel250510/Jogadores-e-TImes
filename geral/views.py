from django.shortcuts import render
from jogadores.models import Jogador
from times.models import Time
# Create your views here.
def geral_home(request):
    if request.method == 'GET':
        jogadores = Jogador.objects.all()
        times = Time.objects.all()
        return render(request, 'geral_home.html', {'jogadores':jogadores, 'times':times})