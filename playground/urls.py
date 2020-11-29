from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'playground'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('students/', views.StudentsView.as_view(), name='students'),
    path('studentsinfo/', views.StudentsInfoView.as_view(), name='studentsinfo'),
    path('hello/', views.hello, name='hello')
]
