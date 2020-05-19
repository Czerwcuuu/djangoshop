from django.shortcuts import render
from django.http import HttpResponse
from .models import Przedmiot

def main(request):
    przedmioty = Przedmiot.objects.all()
    return render(request, 'sklep_app/index.html',{'przedmioty':przedmioty})
