from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'is_public']
    list_display_links = ['title']
    list_editable = ['is_public']
