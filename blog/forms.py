from django import forms
from blog.models import Blog


class PostForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
