
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Recipes


class CommentForm(forms.ModelForm):
    """ Create Comment Form """
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget = forms.Textarea(attrs={'rows': 3})

    class Meta:
        """Get comment model, choose fields to display"""
        model = Comment
        fields = ('body',)


class CreateRecipeForm(forms.ModelForm):
    """ Create Recipe Form """

    class Meta:
        """
        Get recipe model, choose fields to display and add summernote widget
        """
        model = Recipes
        fields = [
            'title',
            'description',
            'preparation',
            'recipe_image',
            'image_alt'
        ]
        widgets = {
            'description': SummernoteWidget(),
            'preparation': SummernoteWidget(),
        }
        labels = {
            'title': 'Recipe Title',
            'description': 'Description',
            'preparation': 'Recipe Preparation',
            'recipe_image': 'Recipe Image',
            'image_alt': 'Describe Image',
        }

    def __init__(self, *args, **kwargs):
        super(CreateRecipeForm, self).__init__(*args, **kwargs)
