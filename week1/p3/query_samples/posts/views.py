# from datetime import datetime, timedelta

# from django.db.models import CharField
from django.db.models import Q, F, When, Case
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
