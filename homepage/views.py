import random

from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_GET
from datetime import datetime, timedelta

from django.views.generic import TemplateView


class ArticleView(TemplateView):
    template_name = 'homepage/article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        args = {
            'article_id': kwargs['article_id'],
            'article_text':
                '\n'.join(
                    [
                        f'{x} - {", ".join(["Lorem ipsum" for y in range(1, random.randint(8, 10))])}'
                        for x in range(1, random.randint(50, 100))
                    ]
                )
        }
        context.update(args)
        return context


class ArticlesView(TemplateView):
    template_name = 'homepage/articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        date_now = datetime.today()
        articles_list = [
            (x.year, x.month, x.day, x.hour, x.minute, x.second) for x in
            [date_now - timedelta(days=x) for x in range(35)]
        ]
        args = {
            'articles': articles_list,
            'client_info':
                f'{self.request.method} to host {self.request.get_host()}'
        }

        context.update(args)
        return context
