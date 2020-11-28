from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'playground'

urlpatterns = [
    # path('', TemplateView.as_view(template_name='playground/index.html'), name='index'),
    path('studentsinfo/', views.StudentsView.as_view(), name='studentsinfo')
]
