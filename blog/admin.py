from django.contrib import admin
from .models import Post
from .models import Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'is_public']
    list_display_links = ['title']
    list_editable = ['is_public']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'author', 'created_at', 'updated_at']
    list_display_links = ['message']
