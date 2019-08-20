from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post, Comment

from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        # So this mean grab all objects. In "__lte", double under score is to mark that
        # Here it "__lte" mean lessthan or equal
        # Syntax: field__lookepvalue = value
        # This is django.db queries




        # order_by('-publish_date')
        # The minor following by publish_date í to detemine that
        # the list will be sorted in the decending order. Which mean
        # the more recent the post is, the higher it appear.

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    # This LoginRequiredMixin is to replace the decorator @login_required
    # in class base view.
    # Decorator login_required can only be used in function base view.

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('created_date')

# Funtions that require a pl match

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.publish()
    return redirect('blog:post_detail', pk = pk)
    # get_object_or_404 ?,
    # Different byw redirect and reverse_lazy, reverse ?

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk = post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form' : form})

    # I dont remember the theory of this commit = False. When to use, When not
    # to ?

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    comment.approve()
    return redirect('blog:post_detail', pk = comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect( 'blog:post_list', pk = post.pk)

    # I think delete() is a method of built in models.Model
    # it's important to notice that the comment pk is different from the post's
    # pk
