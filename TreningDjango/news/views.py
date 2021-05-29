from django.shortcuts import render
from .models import Post

def news_list(request):
    return render(request, 'news/post/list.html',
                  {'posts': Post.objects.all()})
