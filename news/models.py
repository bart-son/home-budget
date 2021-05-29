from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    CATEGORIES = (('IT', 'Informatyka'), ('G', 'Geografia'), ('Z', 'Zdrowie'))
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=10, choices=CATEGORIES, default='Z')
    def __str__(self):
        return self.title
