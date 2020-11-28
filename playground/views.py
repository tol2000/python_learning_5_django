from django.views.generic import ListView

from playground.models import StudentInfo


class StudentsView(ListView):
    template_name = 'playground/studentsinfo.html'
    model = StudentInfo
    context_object_name = 'studentsinfo'
