from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse as HR
def Captain(request):
    return HR('<h1><marquee>Hardik pandya uturaj is captain of MI </h1>')