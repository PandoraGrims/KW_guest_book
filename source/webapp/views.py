from django.shortcuts import render, redirect

from webapp.models import Book, status_choices
from webapp.form import BookForm


def book_list_view(request):
    books = Book.objects.order_by("-created_at")
    context = {"books": books}
    return render(request, "index.html", context)


def book_create(request):
    if request.method == "GET":
        form = BookForm()
        return render(request, "book_create.html", {"status_choices": status_choices, "form": form})
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = Book.objects.create(author=form.cleaned_data.get('author'),
                                       email=form.cleaned_data.get('email'),
                                       description=form.cleaned_data.get('description'))
            return redirect("index", pk=book.pk)
        else:
            return render(request, "book_create.html", {"status_choices": status_choices, "form": form})

#
# def book_create(request):
#     if request.method == "GET":
#         form = BookForm()
#         return render(request, "book_create.html", {"form": form})
#     else:
#         form = BookForm(data=request.POST)
#         if form.is_valid():
#             book = Book.objects.create(author=form.cleaned_data.get('author'),
#                                        email=form.cleaned_data.get('email'),
#                                        text=form.cleaned_data.get('text'))
#             return redirect('index')
#         else:
#             return render(request, "index.html", {"form": form})
