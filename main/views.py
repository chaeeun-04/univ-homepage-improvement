from django.shortcuts import render
from product.models import Category
from pages.models import MenuClick


def index(request):

    all_categories = Category.objects.all()

    for category in all_categories:
        category.recent_posts = category.posts.order_by('-created_at', '-id')[:3]

    top_2_menus = MenuClick.objects.order_by('-click_count')[:2]

    context = {
        'all_categories': all_categories,
        'top_menus': top_2_menus,
    }

    return render(request, 'main/index.html', context)

def matching(request):
    return render(request, 'matching/index.html')
