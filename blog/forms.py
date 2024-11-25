from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'author']
        widgets = {
            'content': SummernoteWidget(), # Allows for rich text editing within content
        }

class CommentForm(forms.ModelForm):
    model = Comment
    fields = ['content, author, date_posted']
