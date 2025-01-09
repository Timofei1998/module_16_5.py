from django.core.paginator import Paginator
from django.shortcuts import render
from .models import News

# Create your views here.
def news_view(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    return render(request, 'task1/news.html', {'news': news})
