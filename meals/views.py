from django.shortcuts import render

# Create your views here.
from .models import Meals as MealsModel


def meal_list(request):
    meal_list = MealsModel.objects.all()

    context = {'meal_list': meal_list, }

    return render(request, 'Meals/list.html', context)


def meal_detail(request, slug):
    pass
