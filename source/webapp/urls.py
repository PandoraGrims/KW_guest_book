from django.urls import path

from webapp.views import book_list_view, book_create

urlpatterns = [
    path('', book_list_view, name="index"),
    path('book/add/', book_create, name="book_create"),
]
