from django.urls import path

from . import views

urlpatterns = [
    path("todos/completed", views.CompletedTodoListAPIView.as_view()),
    
]
