from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):

    search_fields = ['title', 'content']
    list_display = ['__unicode__', 'timestamp', 'updated']

    class Meta:
        model = Post



admin.site.register(Post, PostModelAdmin)