from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html', )

def password(request):
    password1 = ''
    length = int(request.GET.get('length', 12))#applies a defualt of 12
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@£$%^&*()_+'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for x in range(length):
        password1 += random.choice(characters)
    return render(request, 'generator/password.html', {'password': password1})

def destination(request):
    return render(request, 'generator/destination.html')
