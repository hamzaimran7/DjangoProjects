from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def polls(request):
    return HttpResponse("Welcome to the Polls page! Everything you will appear here!")
def download(request):
    return HttpResponse("Welcome to Download Page.\n \t Your Download will begin Shortly!")
def counter(request):
    text= request.GET['text']
    amount_of_words=len(text.split())
    return render (request, 'counter.html', {'amount':amount_of_words})

