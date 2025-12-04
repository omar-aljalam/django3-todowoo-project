from django.urls import path

from . import views

urlpatterns = [
    # Todos
    path("todos/", views.CurrentTodoListAPIView.as_view()),
    path("todos/<int:pk>", views.TodoDetailAPIView.as_view()),
    path("todos/<int:pk>/complete", views.CompleteTodoAPIView.as_view()),
    path("todos/completed", views.CompletedTodoListAPIView.as_view()),

    # Auth
    path("signup/", views.sign_up),
    path("login/", views.login),
]
