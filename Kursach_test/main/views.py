from django.shortcuts import render
from .models import Rim, Lenses, Accessories
# Create your views here.


def home(request):
    rim = Rim.objects.all()
    lenses = Lenses.objects.all()
    accessories = Accessories.objects.all()
    return render(request, 'main/home.html', {'title': 'Главная страница сайта', 'rim': rim, 'lenses': lenses, 'accessories': accessories})


def about_us(request):
    return render(request, 'main/about-us.html')

