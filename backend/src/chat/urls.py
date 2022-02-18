from django.urls import path

from src.chat import views

app_name = 'chat'

urlpatterns = [
    path('<int:pk>/', views.GetMessages.as_view({'get': 'list', 'post': 'create'})),
]
