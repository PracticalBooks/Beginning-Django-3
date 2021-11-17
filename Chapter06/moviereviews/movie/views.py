from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'name':'Greg Lim'})

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

