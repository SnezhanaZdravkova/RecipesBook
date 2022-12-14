from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Recipes(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, max_length=200)
    description = models.TextField()
    preparation = models.CharField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modefy_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = ('Recipes')

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):

    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
