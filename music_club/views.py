from django.shortcuts import render
from .models import Cancion

# Create your views here.
def cancion_list(request):
    canciones = Cancion.objects.all().order_by('title')
    return render(request, 'music_club/cancion_list.html', {'canciones':canciones})

def cancion_new(request):
    pass