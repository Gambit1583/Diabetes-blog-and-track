from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import Post
from .forms import PostForm, CommentForm


class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'

# Post views

# Lists all blog posts

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comeent.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post_html', {'post': post, 'comments': comments, 'comment_form': comment_form})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_detail.html', {'posts': posts})



