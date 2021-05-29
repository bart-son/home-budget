from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created')
    search_fields = ('title', 'content')
    ordering = ('category', 'created')
    last_filter = ('author', 'category', 'created')
    date_hierarchy = 'created'
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)


