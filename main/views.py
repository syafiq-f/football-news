from django.shortcuts import render, redirect, get_object_or_404
from main.forms import NewsForm
from main.models import News

def show_main(request):
    news_list = News.objects.all()

    context = {
        'npm' : '2406439715',
        'name': 'Syafiq Faqih',
        'class': 'PBP C',
        'news_list': news_list
    }

    return render(request, "main.html", context)

def create_news(request):
    form = NewsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_news.html", context)

def show_news(request, id):
    news = get_object_or_404(News, pk=id)
    news.increment_views()

    context = {
        'news': news
    }

    return render(request, "news_detail.html", context)