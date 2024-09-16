from django.http import HttpResponse


def movies(request):
    return HttpResponse("hello there")
