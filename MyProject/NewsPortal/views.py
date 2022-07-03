from django.shortcuts import render
from .models import Post
from datetime import datetime
# Create your views here.

from django.views.generic import ListView,DetailView

class PostsList(ListView):

    model = Post

    ordering = '-time_in'

    template_name = 'posts.html'

    context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class OnePost(DetailView):

    model = Post

    template_name = 'post.html'

    context_object_name = 'post'



