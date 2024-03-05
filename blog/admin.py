from django.contrib import admin
from .models import Post

@admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'authot', 'publish', 'status']
# Register your models here.
