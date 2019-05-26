from django.shortcuts import render


from django.template.loader import render_to_string

from django.shortcuts import HttpResponse

from games.models import Game

from news.models import News

from pages.models import Page



def show_main_page(request):
    gemes =Game.objects.order_by('-id')[:5]
    news = News.objects.all()[:5]
    pages = Page.objects.all()[:5]

    result = render_to_string('index.html',{
        'news' : news,
        'gemes' : gemes,
        'pages' : pages,
    })

    return HttpResponse(result)