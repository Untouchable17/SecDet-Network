from django.urls import path

from src.posts import views

app_name = "feed"

urlpatterns = [
    path("", views.ArticleView.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path("<int:pk>/", views.ArticleView.as_view(
        {'put': 'update', 'delete': 'destroy'}
    )),
    path("<int:pk>/like", views.AddPostLike.as_view()),
    path("<int:pk>/dislike", views.AddPostDislike.as_view()),
    path('comments/', views.CommentAuthorView.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('comments/<int:pk>/', views.CommentAuthorView.as_view(
        {'put': 'update', 'delete': 'destroy'}
    )),
    path('comments_by_post/<int:pk>/', views.CommentView.as_view(
        {'get': 'list'}
    )),

]