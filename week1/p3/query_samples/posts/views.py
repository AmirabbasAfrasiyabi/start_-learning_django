from datetime import datetime, timedelta

# from django.db.models import CharField
from django.db.models import Q ,F
from django.http import HttpResponse
# Create your views here.

# from posts.forms import post_formset, book_formset
from posts.models import Post

def retrieve_posts(request):
    filter_exp = Q()

    if 'title' in request.GET.keys():
        filter_exp &= Q(title__in=request.GET.getlist('title'))

    if 'content' in request.GET.keys():
        filter_exp |= Q(content=request.GET.get('content'))

    posts = Post.objects.filter(~filter_exp)
    # is equal to: posts = Post.objects.exclude(filter_exp)
    message = f'post count: {posts.count()}'
    return HttpResponse()

def retrieve_posts_exclude_sample(request):
    posts = Post.objects.all()

    if 'title' in request.GET.keys():
        posts = posts.exclude(title=request.GET.get('title'))

    posts = posts.order_by('-title', 'content')
    posts = posts.filter(created_date__range=(datetime.now() - timedelta(hours=1), datetime.now()))

    # message = f'post count: {posts.count()}'
    return HttpResponse(posts.only('title').values_list('title', flat=True))

def retrieve_posts_with_equal_content_title(request):
    # python way to find posts with equal content & title
    # posts = []
    # for post in Post.objects.all():
    #     if post.title == post.content:
    #         posts.append(post)

    # db (orm) way to find posts with equal content & title
    posts = Post.objects.filter(title=F('content')).annotate(view_like_avg=F('like_count') + F('view_count'))

    return HttpResponse(posts.values_list('title', 'content', 'view_like_avg'))
