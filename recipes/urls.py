from recipes import views
from django.urls import path


urlpatterns = [
    path('', views.RecipesList.as_view(), name='home'),
    path('create_recipe/', views.CreateRecipe.as_view(), name='create_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
]
