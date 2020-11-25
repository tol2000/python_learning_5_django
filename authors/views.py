from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, TemplateView

from .forms import AuthorForm
from .models import Author


class IndexView(ListView):

    template_name = 'authors/index.html'
    model = Author
    context_object_name = 'authors'


class CreateAuthorView(TemplateView):
    template_name = 'authors/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthorForm()
        return context

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('authors:create'))
        return render(request, self.template_name, {'form': form})
