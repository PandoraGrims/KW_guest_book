from django.shortcuts import render, redirect, get_object_or_404

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
            return redirect("index")
        else:
            return render(request, "book_create.html", {"status_choices": status_choices, "form": form})


def book_update(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == "GET":
        form = BookForm(initial={"author": book.author,
                                 "email": book.email,
                                 "description": book.description,
                                 })
        return render(request, "book_update.html", {"status_choices": status_choices, "form": form})
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.author = request.POST.get("author")
            book.email = request.POST.get("email")
            book.description = request.POST.get("description")
            book.save()
            return redirect("index")
        else:
            return render(request, "book_update.html", {"form": form})


def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == "GET":
        return render(request, "delete_book.html", {"book": book})
    else:
        book.delete()
        return redirect("index")

# def delete_book(request, id):
    # book = get_object_or_404(Book, id=id)
    # if request.method == "GET":
    #     return render(request, "delete_book.html", {"book": book})
    # else:
    #     book.delete()
    #     return redirect("records_view")