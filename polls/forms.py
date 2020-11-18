from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title',  'title_tag', 'author', 'text',)

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'write here ur title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'bpdy': forms.Textarea(attrs={'class': 'form-control'}),
        }