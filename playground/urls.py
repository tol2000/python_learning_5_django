from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'playground'

urlpatterns = [
    # path('', TemplateView.as_view(template_name='homepage/index.html'), name='index'),
    # path('articles/', views.ArticlesView.as_view(), name='articles'),
]
