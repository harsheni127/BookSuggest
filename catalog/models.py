from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True, related_name="books")
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("catalog:book_detail", args=[self.pk])

