from django.urls import path
from . import views
from .views import (
    CreateRecipe, RecipesList,
    RecipeDetail, DeleteComment,
    RecipeLike,
)


urlpatterns = [
    path('', views.RecipesList.as_view(), name='home'),
    # path('your_recipes/', views.YourRecipes.as_view(), name='your_recipes'),
    path('create_recipe', CreateRecipe.as_view(), name='create_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(),
         name='edit_comment'),
    path('comment/<int:pk>/delete', views.DeleteComment.as_view(),
         name='delete_comment'),
    # path('delete_comment/<int:pk>/', views.delete_comment,
    #      name='delete_comment'),
    path('update_recipe/<int:pk>', views.UpdateRecipe.as_view(),
         name='update_recipe'),
    # path("delete/<int:pk>/", views.DeleteRecipe.as_view(),
    #      name="delete_recipe"),
    path('delete_recipe/<int:pk>', views.delete_recipe,
         name='delete_recipe')
]
