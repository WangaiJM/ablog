from django.urls import path
# from . import views
from .views import HomeView, ArticleDetail, AddPostView

urlpatterns = [
    # path('', views.home, name='home')
    path('', HomeView.as_view(), name="home"),
    path('<slug:slug>/<str:id>/', ArticleDetail.as_view(), name="article_detail"),
    path('add-post/', AddPostView.as_view(), name="add_post"),
]
