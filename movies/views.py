from django.http import HttpResponse
from django.shortcuts import render


def movies(request):
    # return HttpResponse("hello there")
    data = {
            'movies': ['movie1', 'movie2']
        }

    return render(
        request, 
        'movies/movies.html', data
    )

def home(request):
    return HttpResponse("home page")
