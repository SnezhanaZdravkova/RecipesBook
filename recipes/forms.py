
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

    def form_valid(self, form):
        messages.success(self.request,
                         "Recipe Successfully Added & Awaiting Approval")
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)
