from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth.mixins import (
# LoginRequiredMixin,
# UserPassesTestMixin
# )
from django.views import generic, View
from django.views.generic import DetailView, CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.db.models import Count
# from django.utils.text import slugify
from django.http import HttpResponseRedirect
from .models import Recipes, Comment
from .forms import CommentForm, CreateRecipeForm


class RecipesList(generic.ListView):
    model = Recipes
    queryset = Recipes.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(DetailView):
    """
    This view is used to display the full recipe details including comments.
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipes.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comment.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipes.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comment.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipes = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class EditComment(UpdateView):
    """ Edit Comments """
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse(
        'recipe_detail', args=[comment.recipe.slug]))


class RecipeLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Recipes, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


# class YourRecipes(View):

#     def get(self, request):
#         if request.user.is_autenticated:
#             recipe = Recipes.objects.filter(author=request.user)


class CreateRecipe(CreateView):
    """This view is used to allow logged in users to create a recipe"""

    model = Recipes
    form_class = CreateRecipeForm
    template_name = 'create_recipe.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request,
                         "Recipe Successfully Added & Awaiting Approval")
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)


class UpdateRecipe(UpdateView):
    """ Edit Recipe """

    model = Recipes
    template_name = 'update_recipe.html'
    form_class = CreateRecipeForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('update_recipe')

    def form_valid(self, form):
        messages.success(self.request, "Recipe Successfully Updated")
        form.instance.author = self.request.user
        return super(UpdateRecipe, self).form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user


def delete_recipe(request, recipes_id):
    """ Delete recipe"""
    recipe = get_object_or_404(Recipes, id=recipes_id)
    recipe.delete()

    return redirect(reverse('home'))
