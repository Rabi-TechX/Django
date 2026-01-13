from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse(" Hello ritik.. <a href='http://127.0.0.1:8000/about'>Link for about section</a> ")
def about(request):
    return HttpResponse(" About ritik.. <a href='/'>Link for home section</a> ")