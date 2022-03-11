from django.shortcuts import render
from django.views import generic
from djresume.models import Blog


class BlogDetailView(generic.DetailView):
    template_name = 'blog.html'
    queryset = Blog.objects.all()
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context
