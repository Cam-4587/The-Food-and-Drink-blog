from django import forms
from django.core.exceptions import ValidationError
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post


class CreateBlogPost(forms.ModelForm):
    """
    Blog post creation form
    """
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', ]