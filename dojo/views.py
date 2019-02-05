# dojo/views.py
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from dojo.forms import PostForm
from .models import Post

def generate_view_fn(model):
    def view_fn(request, id):
        instance = get_object_or_404(model, id=id)
        instance_name = model._meta.model_name
        template_name = '{}/{}_detail.html'.format(model._meta.app_label, instance_name)
        return render(request, template_name, {
            instance_name: instance
        })
    return view_fn

post_detail = generate_view_fn(Post)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # 방법 1
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            # 방법 2
            '''
            post = Post.objects.create(title = form.cleaned_data['title'],
                                        content = form.cleaned_data['content'])
            post.save()
            '''

            # 방법 3
            '''
            post = Post.objects.create(title=form.cleaned_data['title'],
                                       content=form.cleaned_data['content'])
          '''
            # 방법 4
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/') # namespace:name
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')    # namespace:name
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })

def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.rstrip('/').split('/')))
    return HttpResponse(result)
    # numbers = '1/2/3/4/5/6 ...'
    #request: HttpRequest

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다. </p>
    '''.format(name = name))

def post_list2(request):
    name = '공유'
    response = render(request, 'dojo/post_list.html', {'name': name})
    return response


def post_list3(request):
    return JsonResponse({
        'message': '안녕 파이썬&장고',
        'items': ['파이썬', '장고', 'Celary', 'Azure']
    }, json_dumps_params = {'ensure_ascii': False})


def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'test.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
