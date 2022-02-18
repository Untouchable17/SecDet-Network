from django.urls import path

from src.groups import views

app_name = "groups"

urlpatterns = [
    path("", views.GroupsView.as_view({'get': 'list', 'post': 'create'})),
    path("<int:pk>/", views.GroupsView.as_view({'put': 'update', 'delete': 'destroy'})),
    path('<int:pk>/wall/', views.GroupArticleView.as_view(
        {'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}
    )),
    path('<int:pk>/follow/add/', views.AddGroupFollower.as_view()),
    path('<int:pk>/follow/remove/', views.RemoveGroupFollower.as_view()),
    path('follow_list/', views.ShowFollowerGroups.as_view({'get': 'list'})),

]