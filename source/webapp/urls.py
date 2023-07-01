from django.urls import path

from webapp.views import book_list_view

urlpatterns = [
    path('', book_list_view, name="index"),
]
