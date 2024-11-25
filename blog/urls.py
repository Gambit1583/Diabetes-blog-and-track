from . import views
from django.urls import path
from .views import HomePage, post_list

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('', views.post_list, name='post_list'), 
    path('post/<int:id>/', views.post_detail, name='post_detail'), 
    # path('post/new/', views.post_create, name='post_create'), 
    # path('post/<int:id>/edit/', views.post_update, name='post_update'), 
    # path('post/<int:id>/delete/', views.post_delete, name='post_delete'),
]