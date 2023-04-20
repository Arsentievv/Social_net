from django.urls import path

from .views import post_model_create_and_list_view, like_unlike_posts

app_name = 'posts'

urlpatterns =[
    path('', post_model_create_and_list_view, name='main-post-view'),
    path('liked/', like_unlike_posts, name='like-post-view'),
]