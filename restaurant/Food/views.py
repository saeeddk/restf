from django.shortcuts import render
from .models import Food
# Create your views here.

def food_list(request):
    food_list = Food.objects.all()
    context = {
        "Food": food_list
    }
    return render(request, "Food/list.html", context)

def food_detail(request, id):
    food = Food.objects.get(id=id)
    context = {
        "food": food
    }
    return render(request, "Food/detail.html", context)
