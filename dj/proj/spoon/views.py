from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    name = request.GET['name']
    spoon = [1, 2, 3, 4, 5]
    ability = ['ugly', 'clever', 'godness', 'handsome', 'idot']
    random.shuffle(spoon)
    random.shuffle(ability)
    return render(request, 'result.html', {'name': name, 'spoon':spoon, 'ability': ability})