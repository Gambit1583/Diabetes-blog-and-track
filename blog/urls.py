from django.urls import path
from .views import HomePage, post_list, post_detail

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('posts/', post_list, name='post_list'),
    path('post/<int:id>/', post_detail, name='post_detail'), 
    # path('post/new/', views.post_create, name='post_create'), 
    # path('post/<int:id>/edit/', views.post_update, name='post_update'), 
    # path('post/<int:id>/delete/', views.post_delete, name='post_delete'),
]