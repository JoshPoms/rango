from django.http import HttpResponse

def index(request):
	return HttpResponse("Ayy, Hello World <br/> <a href='/rango/about'>About</a>")

def about(request):
	return HttpResponse("This is the about section bitch <br/> <a href='/rango/'>Index</a>")
