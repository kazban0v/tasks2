from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('tasks.urls')),
]
