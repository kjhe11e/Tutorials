from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hola, mundo. Welcome to the site. Enjoy!")

