from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    CATEGORIES = (
        ('IT', 'Informatyka'),
        ('Z', 'Zdrowie'),
        ('G', 'Geografia')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique_for_date='created')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20, choices=CATEGORIES, default='Z')
    def __str__(self):
        return self.title
