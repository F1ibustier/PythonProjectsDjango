from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import UserRegister
from .models import Game, Buyer, News

# Create your views here.

game_list = Game.objects.all()

def main_page(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    context = {'game_list': game_list}
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    context = {'games_list': [0]}
    return render(request, 'fourth_task/cart.html', context)


def news(request):
    # получаем все посты
    news_list = News.objects.all()

    # создаем пагинатор
    paginator = Paginator(news_list, 10)  # 10 постов на странице

    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')

    # получаем посты для текущей страницы
    page_news_list = paginator.get_page(page_number)

    # передаем контекст в шаблон
    return render(request, 'fourth_task/news.html', {'page_news_list': page_news_list})


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        users = Buyer.objects.values_list('name', flat=True)

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse('Пароли не совпадают')
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
            return HttpResponse('Вы должны быть старше 18')
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            return HttpResponse('Пользователь уже существует')
        else:
            Buyer.objects.create(name=username, age=age, balance=1500)
            info['welcome_message'] = f'Приветствуем, {username}!'
        return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'fifth_task/registration_page.html', context = info)

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            users = Buyer.objects.values_list('name', flat=True)

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return HttpResponse('Пароли не совпадают')
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return HttpResponse('Вы должны быть старше 18')
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                return HttpResponse('Пользователь уже существует')
            else:
                Buyer.objects.create(name=username, age=age, balance=1500)
                info['welcome_message'] = f'Приветствуем, {username}!'
            return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form':form})
