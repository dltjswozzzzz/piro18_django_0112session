from django.contrib import admin

# Register your models here.

from server.apps.posts.models import Post

admin.site.register(Post)
