from django.views.generic import ListView

from .models import Author


class IndexView(ListView):

    template_name = 'authors/index.html'
    model = Author
    context_object_name = 'authors'

