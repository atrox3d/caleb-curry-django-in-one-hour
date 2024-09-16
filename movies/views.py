from django.http import HttpResponse


def movies(request):
    return HttpResponse("hello there")

def home(request):
    return HttpResponse("home page")
