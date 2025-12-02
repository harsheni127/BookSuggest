from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.book_list, name="home"),
    path("books/", views.book_list, name="book_list"),
    path("books/add/", views.book_create, name="book_add"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    path("books/<int:pk>/edit/", views.book_edit, name="book_edit"),
    path("books/<int:pk>/delete/", views.book_delete, name="book_delete"),
    path("suggest/", views.suggest_random, name="suggest_random"),
]
