from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    # return HttpResponse("<h1> Hello, World!</h1>")
    return render(request, 'generator/home.html',{'password':'hjkhjkhjkhjk'})

def about(request):
    # return HttpResponse("About Page")
    return render(request, 'generator/about.html')


def password(request):
    # return HttpResponse("Eggs are great!")
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html',{'password':thepassword})