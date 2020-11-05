from django.shortcuts import render
from django.http import HttpRequest
import datetime


def index_page(request: HttpRequest):
    date_now = datetime.datetime.today()
    cookie_last_visit_name = 'last_visit'
    last_visit = request.get_signed_cookie(cookie_last_visit_name, None)
    response = render(request, 'homepage/index.html')
    response.set_cookie(cookie_last_visit_name, date_now)
    return response


def articles(request: HttpRequest):
    return render(request, 'homepage/articles.html')
