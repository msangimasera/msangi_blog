from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('admin/', admin.site.urls),
]