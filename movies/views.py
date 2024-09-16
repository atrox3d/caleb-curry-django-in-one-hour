from django.http import HttpResponse
from django.shortcuts import render


def movies(request):
    # return HttpResponse("hello there")
    data = {
            'movies': [
                {
                    'id': 5,
                    'title': 'Jaws',
                    'year': 1969
                },
                {
                    'id': 6,
                    'title': 'sharknado',
                    'year': 1900
                },
                {
                    'id': 7,
                    'title': 'The Meg',
                    'year': 1980
                },
            ]
        }

    return render(
        request, 
        'movies/movies.html', data
    )

def home(request):
    return HttpResponse("home page")
