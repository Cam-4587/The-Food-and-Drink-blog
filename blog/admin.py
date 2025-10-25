from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = Post
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status',)
    list_display = ('author', 'status', 'created_on', 'updated_on')

admin.site.register(Post, PostAdmin)