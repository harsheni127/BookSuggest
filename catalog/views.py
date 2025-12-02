from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Genre
from django.db.models import Q
from django import forms
from django.contrib.auth.decorators import login_required
import random

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "rating", "genres"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "genres": forms.SelectMultiple(),
        }

def book_list(request):
    q = request.GET.get("q", "").strip()
    author_q = request.GET.get("author", "").strip()
    genre = request.GET.get("genre", "")

    books = Book.objects.all().order_by("-added_at")
    if q:
        books = books.filter(Q(title__icontains=q) | Q(description__icontains=q))
    if author_q:
        books = books.filter(author__icontains=author_q)
    if genre:
        books = books.filter(genres__name=genre)

    from django.core.paginator import Paginator
    paginator = Paginator(books.distinct(), 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    genres = Genre.objects.all()
    context = {
        "books": page_obj,
        "q": q,
        "author_q": author_q,
        "genres": genres,
        "selected_genre": genre,
    }
    return render(request, "catalog/book_list.html", context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "catalog/book_detail.html", {"book": book})

def suggest_random(request):
    count = Book.objects.count()
    book = None
    if count:
        index = random.randint(0, count - 1)
        book = Book.objects.all()[index]
    return render(request, "catalog/suggest.html", {"book": book})

@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            b = form.save()
            return redirect("catalog:book_detail", pk=b.pk)
    else:
        form = BookForm()
    return render(request, "catalog/book_form.html", {"form": form, "create": True})

@login_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            b = form.save()
            return redirect("catalog:book_detail", pk=b.pk)
    else:
        form = BookForm(instance=book)
    return render(request, "catalog/book_form.html", {"form": form, "create": False})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("catalog:book_list")
    return render(request, "catalog/book_confirm_delete.html", {"book": book})


