from django.contrib.auth import login
from django.contrib.auth.models import User

from .models import Post, Comment
from .forms import CommentForm, DraftForm, PostForm, UserForm
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, "blogi/post_list.html", stuff_for_frontend)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blogi/post_detail.html', stuff_for_frontend)

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit= False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        stuff_for_frontend = {'form': form}
        return render(request, 'blogi/post_edit.html', stuff_for_frontend)

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form}
    return render(request, 'blogi/post_edit.html', stuff_for_frontend)

@login_required
def post_draft_list(request):
    draft_list = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    stuff_for_frontend = {'draft_list': draft_list}
    return  render(request, 'blogi/post_draft_list.html', stuff_for_frontend)

@login_required
def post_draft_edit(request, pk):
    post_draft = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = DraftForm(request.POST, instance = post_draft)
        if form.is_valid():
            post_draft = form.save(commit=False)
            post_draft.author = request.user
            post_draft.save()
            return redirect('post_draft_detail',pk=post_draft.pk)
    else:
        form = DraftForm(instance=post_draft)
        stuff_for_frontend = {'post_draft': form}
    return render(request, 'blogi/post_draft_edit.html', stuff_for_frontend)

@login_required
def post_draft_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blogi/post_draft_detail.html', stuff_for_frontend)

@login_required
def post_draft_new(request):
    if request.method == 'POST':
        form = DraftForm(request.POST)
        if form.is_valid():
            post = form.save(commit= False)
            post.author = request.user
            post.save()
            return redirect('post_draft_detail', pk=post.pk)
    else:
        form = DraftForm()
        stuff_for_frontend = {'post_draft': form}
        return render(request, 'blogi/post_draft_edit.html', stuff_for_frontend)

@login_required
def post_delete(request,pk):
    post_to_delete = get_object_or_404(Post, pk=pk)
    post_to_delete.delete()
    return redirect('post_list')

@login_required
def publish_draft(request, pk):
    post_to_publish = get_object_or_404(Post, pk=pk)
    post_to_publish.published_date = timezone.now()
    post_to_publish.save()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment  = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
        return render(request, 'blogi/add_comment_to_post.html',{'form': form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'blogi/signup.html', {'form':form})