from django.urls import path
from . import views
urlpatterns = [
    path('geral_home/', views.geral_home, name='geral_home')
]