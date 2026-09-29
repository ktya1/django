from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from posts.models import Post


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                title = form.cleaned_data['title'],
                text = form.cleaned_data['text'],
                author = request.user,
            )

            return redirect('posts')
    else:
        form = PostForm()

    return render(request, 'posts/create.html',  {'form': form})

def read_post(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'posts/read.html',  {'post': post})



def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})



def update_post():
    ...

def delete_post():
    ...


