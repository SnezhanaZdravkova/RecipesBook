from django.shortcuts import render
from django.views import generic
from .models import Recipes


class RecipesList(generic.ListView):
    model = Recipes
    queryset = Recipes.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
