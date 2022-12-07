from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# def home(request):
#     return render(request, 'home.html', {})
class HomeView(ListView):
    model: Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.order_by('id')