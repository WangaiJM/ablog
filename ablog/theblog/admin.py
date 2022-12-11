from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    search_fields = ['author__username', 'title', 'created_at']
    list_display = ['title', 'author', 'created_at']
    list_filter = ['author', 'created_at']
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Post, PostAdmin)