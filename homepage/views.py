from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_GET
from datetime import datetime, timedelta


def index_page(request: HttpRequest):
    date_now = datetime.today()
    cookie_last_visit_name = 'last_visit'
    # last_visit = request.get_signed_cookie(cookie_last_visit_name, None)
    days = [
        date_now - timedelta(days=x) for x in range(35)
    ]
    args = {
        'days': days,
        'days_str': '\n'.join([str(x) for x in days])
    }
    response = render(request, 'homepage/index.html', args)
    response.set_cookie(cookie_last_visit_name, date_now)
    return response


@require_GET
def articles(request: HttpRequest):
    date_now = datetime.today()
    articles_list = [
        str(date_now - timedelta(days=x)) for x in range(35)
    ]
    args = {
        'articles': articles_list,
        'client_info':
            f'{request.method} to host {request.get_host()}'
    }
    return render(request, 'homepage/articles.html', args)
