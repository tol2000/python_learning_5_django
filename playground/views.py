from django.http import HttpResponse

from django.views.generic import ListView, TemplateView

from playground.models import Student, StudentInfo, Article


class IndexView(TemplateView):
    template_name = 'playground/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context


class StudentsView(ListView):
    template_name = 'playground/students.html'
    model = Student
    context_object_name = 'students'


class StudentsInfoView(ListView):
    template_name = 'playground/studentsinfo.html'
    model = StudentInfo
    context_object_name = 'studentsinfo'


def hello(request):
    return HttpResponse('Hello, playground! :)')
