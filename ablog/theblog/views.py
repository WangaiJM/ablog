from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


# def home(request):
#     return render(request, 'home.html', {})
class HomeView(ListView):
    model: Post
    template_name = 'home.html'
    queryset = Post.objects.all()

class ArticleDetail(DetailView):
    model: Post
    template_name = 'article-detail.html'
    queryset = Post.objects.all()

class AddPostView(CreateView):
    model: Post
    template_name = 'add_post.html'
    queryset = Post.objects.all()
    fields = '__all__'