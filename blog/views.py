from django.shortcuts import render
# from django.http import HttpResponse

news = [
    {
        'title': 'Наша первая запись',
        'text': 'Просто большой текст',
        'date': '1 января 2020',
        'avtor': 'Георгий',
    },
    {
        'title': 'Наша вторая запись',
        'text': 'Просто большой текст для нашей второй записи',
        'date': '10 января 2020',
        'avtor': '',
    },
]


def home(request):
    data = {
        'news': news,
        'title': 'Главная страница блога',
    }
    return render(request, 'blog/home.html', data)

def contacti(request):
    return render(request, 'blog/contacti.html', {'title': 'Страница с контакроми.'})

def example(request):
    return render(request, 'blog/index.html', {'title': 'Example.'})

def contact(request):
    return render(request, 'blog/contact.html')

def colt(request):
    return render(request, 'blog/colt.html')
