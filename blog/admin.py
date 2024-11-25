from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from .forms import PostForm

# Search and list display for blog posts

class PostAdmin(admin.ModelAdmin): 
    form = PostForm
    list_display = ('title', 'date_posted', 'author') 
    search_fields = ('title', 'content', 'author')

# Registered models

admin.site.register(Post, PostAdmin)