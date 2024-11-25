from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
from .forms import PostForm

# Search and list display for blog posts

class PostAdmin(admin.ModelAdmin): 
    form = PostForm
    list_display = ('title', 'date_posted', 'author') 
    search_fields = ('title', 'content', 'author')
    list_filter = ('date_posted', 'author') 
    fields = ('title', 'content', 'image', 'author', 'date_posted')

    def save_model(self, request, obj, form, change):
        if not obj.pk: # Only sets the author during first save
            obj.author = request.user
        super().save_model(request, obj, form, change)

# Registered models

admin.site.register(Post, PostAdmin)