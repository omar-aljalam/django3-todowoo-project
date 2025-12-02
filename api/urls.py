from django.urls import path

from . import views

urlpatterns = [
    path("todos/", views.CurrentTodoListAPIView.as_view()),
    path("todos/<int:pk>", views.TodoDetailAPIView.as_view()),
    path("todos/<int:pk>/complete", views.CompleteTodoAPIView.as_view()),
    path("todos/completed", views.CompletedTodoListAPIView.as_view()),
]
