from django.db import models
from .models import Book

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year.year})"

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    class Meta:
        permissions = [
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_view", "Can view book"),
            ("can_delete", "Can delete book"),
        ]