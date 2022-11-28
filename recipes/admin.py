from django.contrib import admin
from .models import Recipes
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipes)
class RecipesAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
