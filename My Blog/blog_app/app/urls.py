from django.urls import path
from .views import HomePage, PostDetailed, BlogCreateView, Blogupdate, BlogDelete

urlpatterns = [
    path('',HomePage.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailed.as_view(), name='post_detailed'),
    path('post/new/',  BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', Blogupdate.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDelete.as_view(), name='post_delete')
]