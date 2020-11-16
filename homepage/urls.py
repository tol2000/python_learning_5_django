from django.urls import path, include
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index_page, name='index'),
    path('articles/', views.articles, name='articles'),
    path('articles/<str:article_id>', views.article, name='articles')
]
