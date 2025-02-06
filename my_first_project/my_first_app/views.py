from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
def home(request):
    template = loader.get_template('firstpage.html')
    table = FirstModel()
    for i in range(1,5):
        table.firstname = f'raja{i}'
        table. lastname = 'kavin'
        table.save()
    print(table.objects.all())
    return HttpResponse(template.render())

