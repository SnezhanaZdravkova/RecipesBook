from recipes import views
from django.urls import path
# from .views import (
#     RecipesList,
#     CreateRecipe,
#     RecipeDetail,
#     RecipeLike,
# )


urlpatterns = [
    path('', views.RecipesList.as_view(), name='home'),
    path('create_recipe/', views.CreateRecipe.as_view(), name='create_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_likes'),
    path('edit_comment/<int:pk>',
         views.EditComment.as_view(), name='edit_comment'),
    path('update_recipe/<int:pk>',
         views.UpdateRecipe.as_view(), name='update_recipe'),
    path('delete_recipe/<int:recipe_id>',
         views.delete_recipe, name='delete_recipe')
]
