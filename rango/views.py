from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "I'm a little fuck boi"}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse("This is the about section bitch <br/> <a href='/rango/'>Index</a>")
