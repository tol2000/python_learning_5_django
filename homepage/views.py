# from django.shortcuts import render
from django.http import HttpResponse


def index_page(request):
    return HttpResponse(f'<h1> Index of homepage </h1>')
