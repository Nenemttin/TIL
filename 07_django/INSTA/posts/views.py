from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Post, Image, HashTag
from .forms import PostModelForm, ImageModelForm, CommentModelForm


@login_required
@require_http_methods(['GET', 'POST'])
def create_post(request):
    # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
    if request.method == 'POST':
        # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
        # ModelForm(data, files) - default
        post_form = PostModelForm(request.POST)
        # Data 검증을 한다.
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            # Create HashTag => <input name='tags'>
            content = post_form.cleaned_data.get('content')
            words = content.split(' ') # 띄어쓰기 기준으로 split
            for word in words:
                if word[0] == '#':
                    word = word[1:]
                    tag = HashTag.objects.get_or_create(content=word) # (HashTagobj, True or False)
                    post.tags.add(tag[0])
                    if tag[1]:
                        messages.add_message(request, messages.SUCCESS, f'#{tag[0].content}태그를 처음으로 추가하셨어요! :)')
            for image in request.FILES.getlist('file'): # 여러 장의 사진은 리스트로 저장되어 들어온다.
                request.FILES['file'] = image
                image_form = ImageModelForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False) # ForeignKey 가 없는 상태
                    image.post = post
                    image.save()
            return redirect('posts:post_list')

    # GET 방식으로 요청이 오면,
    else:
        # 새로운 Post 용 form 을 만든다.
        post_form = PostModelForm()
    image_form = ImageModelForm()

    # 사용자에게 html 과 form을 만든다.
    return render(request, 'posts/form.html', {
        'post_form': post_form,
        'image_form': image_form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user: # 지금 수정하려는 post 작성자가 요청 보낸 사람이냐?
        if request.method == 'POST':
            post_form = PostModelForm(request.POST, instance=post)
            if post_form.is_valid():
                post_form.save()
                # update HashTag
                post.tags.clear() # 기존 태그 다 날리기
                content = post_form.cleaned_data.get('content')
                words = content.split(' ')  # 띄어쓰기 기준으로 split
                for word in words:
                    if word[0] == '#':
                        word = word[1:]
                        tag = HashTag.objects.get_or_create(content=word)  # (HashTagobj, True or False)
                        post.tags.add(tag[0])
                return redirect('posts:post_list')
        else:
            post_form = PostModelForm(instance=post)
    else: # 작성자와 요청 보낸 user 가 다르다면
        # 403 : Forbidden 금지됨!
        return redirect('posts:post_list')

    return render(request, 'posts/form.html', {
        'post_form': post_form
    })


@require_GET
def post_list(request):
    if request.GET.get('next'):
        return redirect(request.GET.get('next'))
    posts = Post.objects.all()
    comment_form = CommentModelForm()

    return render(request, 'posts/list.html', {
        'posts': posts,
        'comment_form': comment_form,
    })


@login_required
@require_POST
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentModelForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))
    # TODO else: => What if comment is not valid?


@login_required
@require_POST
def toggle_like(request, post_id):
    if request.is_ajax():
        user = request.user
        post = get_object_or_404(Post, id=post_id)
        is_active = True
        # if post.like_users.filter(id=user.id): # 찾으면, [value] / 없으면 []
        if user in post.like_users.all():
            post.like_users.remove(user)
            is_active = False
        else:
            post.like_users.add(user)

        return JsonResponse({
            'likeCount': post.like_users.count(),
            'is_active': is_active,
        })
    else:
        return HttpResponseBadRequest()

@require_GET
def tag_posts_list(request, tag_name):
    tag = get_object_or_404(HashTag, content=tag_name)
    posts = tag.posts.all()
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html', {'posts': posts, 'comment_form': comment_form, 'h1': f'#{tag}를 포함한 posts 입니다.'})
