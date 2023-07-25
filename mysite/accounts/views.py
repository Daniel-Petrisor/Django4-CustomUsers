from django.shortcuts import render
from django.http import HttpResponse


# Pagina di registrazione
def register(request):
    return HttpResponse("Pagina di registrazione")

# Pagina di accesso
def login(request):
    return HttpResponse("Pagina di accesso")
