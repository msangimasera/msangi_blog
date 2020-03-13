from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, "blogi/post_list.html", stuff_for_frontend)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blogi/post_detail.html', stuff_for_frontend)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit= False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        stuff_for_frontend = {'form': form}
        return render(request, 'blogi/post_edit.html', stuff_for_frontend)
