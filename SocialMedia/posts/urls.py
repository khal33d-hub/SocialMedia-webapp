from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    path('', views.PostList.as_view(), name="all"),
    path("new/", views.CreatePost.as_view(), name="create"),
    path("by/<username>/",views.UserPosts.as_view(),name="for_user"),
    path("by/<username>/<int:pk>/",views.PostDetail.as_view(),name="single"),
    path("delete/<int:pk>/",views.DeletePost.as_view(),name="delete"),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

]
