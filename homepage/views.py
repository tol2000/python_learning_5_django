from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_GET
import datetime


def index_page(request: HttpRequest):
    date_now = datetime.datetime.today()
    cookie_last_visit_name = 'last_visit'
    last_visit = request.get_signed_cookie(cookie_last_visit_name, None)
    response = render(request, 'homepage/index.html')
    response.set_cookie(cookie_last_visit_name, date_now)
    return response


@require_GET
def articles(request: HttpRequest):
    articles_list = [
        f'Article # {x}' for x in range(1, 8)
    ]
    args = {
        'articles': articles_list,
        'client_info':
            f'{request.method} to host {request.get_host()}'
    }
    return render(request, 'homepage/articles.html', args)
