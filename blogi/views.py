from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts' : posts}
    return render(request, "blogi/post_list.html", stuff_for_frontend)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk);
    stuff_for_frontend = {'post': post}
    return render(request, 'blogi/post_detail.html', stuff_for_frontend)