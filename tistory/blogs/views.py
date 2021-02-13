from django.shortcuts import render, get_object_or_404, redirect
from users.decorators import login_required
from django.urls import reverse
from .models import Post, Comment
from users.models import User
from django.http import HttpResponseRedirect
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts_list.html', context={'posts':posts})

def post_detail(request, post_id):
    user = User.objects.get(email=(request.session.get('user')))
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment.objects.filter(post=post_id)
    is_liked = False

    if post.likes.filter(id=user.id).exists():
        is_liked = True

    return render(request, 'post_detail.html', context={'post':post, 'comments': comment, 'is_liked':is_liked, 'total_likes': post.total_likes()})

def post_like(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    user = User.objects.get(email=(request.session.get('user')))
    is_liked = post.likes.filter(id=user.id).exists()

    if is_liked:
        post.likes.remove(user)
    else:
        post.likes.add(user)

    return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))
@login_required
def post_write(request):
    errors = []
    if request.method =='POST':
        user = User.objects.get(email=(request.session.get('user')))
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        image = request.FILES.get('image')

        if not title:
            errors.append("제목을 입력해주세요.")

        if not content:
            errors.append("내용을 입력해주세요.")

        if not errors:
            post = Post.objects.create(user=user, title=title, content=content, image=image)
            return redirect(reverse('post_detail', kwargs={'post_id':post.id}))

    return render(request, 'post_write.html', {'errors':errors})

@login_required
def comment_write(request):
    errors = []
    if request.method =='POST':
        user = User.objects.get(email=(request.session.get('user')))
        post_id = request.POST.get('post_id', '').strip()
        post = Post.objects.get(pk=post_id)
        content = request.POST.get('content', '').strip()

        if not content:
            errors.append("댓글을 입력해주세요.")

        if not errors:
            comment = Comment.objects.create(user=user, post=post, content=content)
            return redirect(reverse('post_detail', kwargs={'post_id':comment.post.id}))

    return render(request, 'post_detail.html', {'post':post, 'errors':errors})