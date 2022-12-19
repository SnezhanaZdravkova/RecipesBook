
from .models import Comment, Recipes
from django import forms
from django_summernote.widgets import SummernoteWidget


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
        ]
        widgets = {
            'description': SummernoteWidget(),
            'preparation': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(CreateRecipeForm, self).__init__(*args, **kwargs)
