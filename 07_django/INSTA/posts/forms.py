from django import forms
from .models import Post, Image


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file', ]
        widgets = {
            'file': forms.FileInput(attrs={'multiple': True})
        }
