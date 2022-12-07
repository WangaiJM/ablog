from django.urls import path
# from . import views
from .views import HomeView, ArticleDetail

urlpatterns = [
    # path('', views.home, name='home')
    path('', HomeView.as_view(), name="home"),
    path('article/<slug:slug>/', ArticleDetail.as_view(), name="article_detail")
]
