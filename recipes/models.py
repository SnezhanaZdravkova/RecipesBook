from django.db import models
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save,
    pre_delete,
    post_delete,
    m2m_changed,
    )
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Recipes(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, max_length=200)
    excerpt = models.TextField(blank=True)
    description = models.TextField()
    preparation = models.CharField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modefy_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        """Get url after user adds/edits recipe"""
        return reverse('your_recipes', kwargs={'id': self.id})


# I have got the idea for slugify from slagoverflow:
# https://stackoverflow.com/questions/50436658/how-to-auto-generate-slug-from-my-album-model-in-django-2-0-4
@receiver(pre_save, sender=Recipes)
def recipes_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


# @receiver(pre_delete, sender=Recipes)
def recipes_pre_delete(sender, instance, *args, **kwargs):
    print(f"{instance.id} will be removed")


# @receiver(post_delete, sender=Recipes)
def recipes_post_delete(sender, instance, *args, **kwargs):
    print(f"{instance.id} has removed")


# @receiver(m2m_changed, sender=Recipes.likes.through)
def recipe_likes_changed(sender, instance, action, model, pk__set, *args, **kwargs):
    # print(args, kwargs)
    print(action)
    if action == 'pre_add':
        print("Was added")
        qs = model.objects.filter(pk__set=pk__set)
        print(qs.count())


class Comment(models.Model):

    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE,
                                related_name='comment')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
