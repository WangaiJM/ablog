from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm


# def home(request):
#     return render(request, 'home.html', {})
class HomeView(ListView):
    model: Post
    template_name = 'home.html'
    queryset = Post.objects.all()
    # queryset = Post.objects.all().order_by('-created_at')[:2]

class ArticleDetail(DetailView):
    model: Post
    template_name = 'article-detail.html'
    queryset = Post.objects.all()

class AddPostView(CreateView):
    model: Post
    form_class = PostForm
    template_name = 'add_post.html'
    queryset = Post.objects.all()
    # fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model: Post
    form_class = PostForm
    template_name = 'edit_post.html'
    queryset = Post.objects.all()
