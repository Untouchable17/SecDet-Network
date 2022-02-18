from django.urls import path

from src.auth_system import views

app_name = "profile"

urlpatterns = [
    path('<int:pk>/', views.ProfileView.as_view()),
    path('<int:pk>/update/', views.ProfileEdit.as_view()),
    path('<int:pk>/follower/add/', views.AddFollower.as_view()),
    path('<int:pk>/follower/remove/', views.RemoveFollower.as_view()),
]