from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from .models import Post, Comment
from .forms import PostForm

# Search and list display for blog posts
class PostAdmin(admin.ModelAdmin): 
    form = PostForm
    list_display = ('title', 'date_posted', 'author') 
    search_fields = ('title', 'content', 'author')
    list_filter = ('date_posted', 'author') 
    fields = ('title', 'extract', 'content', 'image', 'author', 'date_posted')  # Include extract field

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},  # Use CKEditor widget for text fields
    }

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only sets the author during the first save
            obj.author = request.user
        super().save_model(request, obj, form, change)

# Registered models
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
