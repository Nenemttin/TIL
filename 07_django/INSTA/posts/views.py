from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Post, Image
from .forms import PostModelForm, ImageModelForm


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
            # 통과하면 저장한다.
            post = post_form.save()
            for image in request.FILES.getlist('file'): # 여러 장의 사진은 리스트로 저장되어 들어온다.
                request.FILES['file'] = image
                image_form = ImageModelForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False) # ForeignKey 가 없는 상태
                    image.post = post
                    image.save()
            return redirect('posts:post_list')
        else:
            # 실패하면, 다시 data 입력 form 을 준다.
            pass
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
    if request.method == 'POST':
        post_form = PostModelForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:post_list')
        else:
            pass
    else:
        form = PostModelForm(instance=post)
    return render(request, 'posts/form.html', {
        'post_form': post_form
    })


@require_GET
def post_list(request):
    if request.GET.get('next'):
        return redirect(request.GET.get('next'))
    posts = Post.objects.all()

    return render(request, 'posts/list.html', {
        'posts': posts,
    })



