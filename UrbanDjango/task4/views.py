from django.shortcuts import render

# Create your views here.
game_dict = {'games': ["Atomic Heart", "Cyberpunk 2077"]}

def main_page(request):
    return render(request, 'fourth_task/platform.html')

def games(request):
    context = {'game_dict': game_dict,}
    return render(request, 'fourth_task/games.html', context)

def cart(request):
    context = {'games_dict': [0]}
    return render(request, 'fourth_task/cart.html', context)

