from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, Post


def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'product/content_list.html', context)


def search_results(request):
    query = request.GET.get('q')
    all_results = []

    search_posts = []

    if query:
        search_posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

        for post in search_posts:
            all_results.append({
                'type': post.category.name,
                'title': post.title,
                'id': post.id
            })

    else:
        query = ""

    context = {
        'query': query,
        'results': all_results,
    }
    return render(request, 'product/search_results.html', context)


def detail(request, content_id):
    post = get_object_or_404(Post, pk=content_id)
    context = {
        'post': post
    }
    return render(request, 'product/detail.html', context)