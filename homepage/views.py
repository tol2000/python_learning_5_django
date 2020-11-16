import random

from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_GET
from datetime import datetime, timedelta


def index_page(request: HttpRequest):
    date_now = datetime.today()
    cookie_last_visit_name = 'last_visit'
    # last_visit = request.get_signed_cookie(cookie_last_visit_name, None)
    response = render(request, 'homepage/index.html')
    response.set_cookie(cookie_last_visit_name, date_now)
    return response


@require_GET
def articles(request: HttpRequest):
    date_now = datetime.today()
    articles_list = [
        (x.year, x.month, x.day, x.hour, x.minute) for x in [date_now - timedelta(days=x) for x in range(35)]
    ]
    args = {
        'articles': articles_list,
        'client_info':
            f'{request.method} to host {request.get_host()}'
    }
    return render(request, 'homepage/articles.html', args)


@require_GET
def article(request: HttpRequest, article_id):
    args = {
        'article_id': article_id,
        'article_text': '\n'.join([f'{x} - article_id' for x in range(1, random.randint(50, 100))])
    }
    return render(request, 'homepage/article.html', args)
