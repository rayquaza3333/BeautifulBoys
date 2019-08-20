from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'text',)
        widgets ={
            'title' : forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }   # The post class is only suitable for Post class

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text',)

        widgets ={
            'author' : forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

# Set up the form widgets to correspond to CSS classes ?
# We can style some particular widgets using attribute to the Meta class.
# OK so that mean widgets need to be post as an attribute when inherrit some
# fields from models. Widgets parrameter of form create method happen when
# create forms in froms.py
