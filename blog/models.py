from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField
import uuid
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    image = CloudinaryField(
        'image', default='placeholder', blank=True, null=True
    )
    intro = models.CharField(blank=True, max_length=150)
    content = RichTextUploadingField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | {self.author}"

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    id = models.CharField(
        max_length=100, default=uuid.uuid4,
        unique=True, primary_key=True, editable=False
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.author} | {self.post}"


class Reply(models.Model):
    reply = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='reply'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="replier"
    )
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    id = models.CharField(
     max_length=100, default=uuid.uuid4, unique=True,
     primary_key=True, editable=False
    )

    def __str__(self):
        return f"{self.author} | {self.reply}"
