from . import views
from django.urls import path
# from .views import (
#     RecipesList,
#     CreateRecipe,
#     RecipeDetail,
#     RecipeLike,
# )
# app_name = 'recipes'


urlpatterns = [
    path('', views.RecipesList.as_view(), name='home'),
    # path('your_recipes/', views.YourRecipes.as_view(), name='your_recipes'),
    path('create_recipe/', views.CreateRecipe.as_view(), name='create_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_likes'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(),
         name='edit_comment'),
    path('delete_comment/<int:comment_id>', views.delete_comment,
         name='delete_comment'),
    path('update_recipe/<int:pk>', views.UpdateRecipe.as_view(),
         name='update_recipe'),
    path('delete_recipe/<int:recipe_id>', views.delete_recipe,
         name='delete_recipe')
]
