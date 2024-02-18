from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jogadores/', include('jogadores.urls'), name='jogadores'),
    path('times/', include('times.urls'), name='times'),
    path('geral/', include('geral.urls'), name='geral')
]
