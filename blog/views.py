from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 3번째 매개변수 -> posts(Post 객체) 전달
    return render(request, 'blog/post_list.html', {'posts' : posts})