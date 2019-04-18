from django import forms
from .models import Post, Image, Comment


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content',]


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file', ]
        widgets = {
            'file': forms.FileInput(attrs={'multiple': True})
        }


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]