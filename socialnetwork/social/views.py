from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import PostForm

class PostListView(View):#put methods for each http request you need to handle
    def get(self, request,*args, **kwargs):#handle any get requests that comes to this url
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'social/post_list.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }
        return render(request, 'social/post_list.html', context)
# Create your views here.
