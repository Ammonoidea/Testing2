from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hello world")

def frontPage(request):
	return HttpResponse('This is the frontpage, yo! <a href=\'http://127.0.0.1:8000/rango/\'>""rango""</a>')

def about(request):
		return HttpResponse('Rango Says: Here is the about page')
