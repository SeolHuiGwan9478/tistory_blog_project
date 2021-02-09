from django.shortcuts import render, get_object_or_404, redirect
from users.decorators import login_required
from django.urls import reverse
from .models import Post
from users.models import User
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts_list.html', context={'posts':posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', context={'post':post})

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