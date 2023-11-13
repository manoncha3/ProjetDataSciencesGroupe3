from django.http import HttpResponse


def base(request):
    return HttpResponse("You're at the base page.")

def home(request):
    return HttpResponse("You're at the home page.")

def index(request):
    return HttpResponse("You're at the index page.")