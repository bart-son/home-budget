from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created')
    search_fields = ('title', 'content')
    ordering = ('category', 'created')
    list_filter = ('author', 'category', 'created')
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)