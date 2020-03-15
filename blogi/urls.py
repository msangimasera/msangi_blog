from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('admin/', admin.site.urls),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('drafts/new', views.post_draft_new, name='post_draft_new'),
    path('drafts/<int:pk>/', views.post_draft_detail, name='post_draft_detail'),
    path('drafts/<int:pk>/edit/', views.post_draft_edit, name='post_draft_edit'),
    path('drafts/<int:pk>/publish', views.publish_draft, name='publish_draft'),
]