from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

# from webapp.form import BookForm
from webapp.models import Book, status_choices


def book_list_view(request):
    books = Book.objects.order_by("-data_field")
    context = {"books": books}
    return render(request, "index.html", context)
