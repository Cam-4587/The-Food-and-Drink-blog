from django import forms
from django.core.exceptions import ValidationError
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post, Profile


class CreateBlogPost(forms.ModelForm):
    """
    Blog post creation form
    """
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', ]


class UpdateProfileForm(forms.ModelForm):
    """
    Form to alter user's profile
    """
    model = Profile

    widgets = {
        'bio': CKEditorUploadingWidget(
                attrs={"class": "form-control"},
            ),
    }

    class Meta:
        model = Profile
        fields = ['image', 'bio']