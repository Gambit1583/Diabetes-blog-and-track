from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Post
from .forms import PostForm, CommentForm

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

# Lists all blog posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# Post detail view without login required
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', id=post.id)
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})










