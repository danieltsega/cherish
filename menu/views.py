from django.shortcuts import render, get_object_or_404
from .models import Category, Food

def home(request):
    categories = Category.objects.prefetch_related('foods').all()
    return render(request, 'menu/home.html', {'categories': categories})