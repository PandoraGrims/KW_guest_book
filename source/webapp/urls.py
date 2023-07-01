from django.urls import path

from webapp.views import book_list_view, book_create, book_update, task_delete

urlpatterns = [
    path('', book_list_view, name="index"),
    path('book/add/', book_create, name="book_create"),
    path('book/<int:pk>/update', book_update, name="book_update"),
    path('book/<int:pk>/delete', task_delete, name="task_delete"),
]
