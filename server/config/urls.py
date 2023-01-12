from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('server.apps.posts.urls')),
    path('admin/', admin.site.urls),
]