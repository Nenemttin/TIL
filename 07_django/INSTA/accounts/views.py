from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth import get_user_model
from .models import User
from posts.forms import CommentModelForm



# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('posts:post_list')

    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def log_in(request):
    # 우선, 사용자가 로그인 되어 있는지?
    if request.user.is_authenticated:
        return redirect('posts:post_list')

    # 로그인 안되어 있다면,
    if request.method == 'POST': # 사용자가 로그인 데이터를 넘겼을 때
        form = CustomUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Do login
            user = form.get_user()
            login(request, form.get_user())
            messages.add_message(request, messages.SUCCESS, f'Welcome back, {user.username}')
            messages.add_message(request, messages.SUCCESS, f'Last login, {user.last_login}')
            return redirect(request.GET.get('next') or 'posts:post_list')
    # 사용자가 로그인 화면을 요청할 때
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def log_out(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, '안녕히 가세요 :)')
    return redirect('posts:post_list')


def user_detail(request, username):
    user_info = User.objects.get(username=username)
    user_posts = user_info.post_set.all()
    return render(request, 'accounts/user_detail.html', {'user_info': user_info, 'user_posts': user_posts, 'comment_form': CommentModelForm(), })


@login_required
@require_POST
def toggle_follow(request, username):
    sender = request.user
    receiver = get_object_or_404(User, username=username)

    if sender != receiver:
        if receiver in sender.followings.all():
            # unfollow
            sender.followings.remove(receiver)
        else:
            # follow
            sender.followings.add(receiver)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))
