from django.urls.conf import path
from posts import views

app_name = "posts"

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
]