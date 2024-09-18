from turtle import title
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

# data = { 'movies': [ { 'id': 5, 'title': 'Jaws', 'year': 1969 }, { 'id': 6, 'title': 'sharknado', 'year': 1900 }, { 'id': 7, 'title': 'The Meg', 'year': 1980 }, ] }

def home(request):
    return HttpResponse("home page")

def movies(request):
    # return HttpResponse("hello there")
    data = Movie.objects.all()
    return render(
        request, 
        'movies/movies.html', 
        {'movies': data}
    )

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(
        request,
        'movies/detail.html',
        {'movie': data}
    )

def add(request:HttpRequest):

    title = request.POST.get('title')
    year = request.POST.get('year')

    if all(x is not None for x in (title, year)):
        Movie(title=title, year=year).save()
        return HttpResponseRedirect('/movies')

    return render(
        request,
        'movies/add.html'
    )
