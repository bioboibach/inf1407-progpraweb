from django.urls.conf import path
from reviews import views

app_name = "reviews"

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='review-list'),
    path('create/', views.ReviewCreateView.as_view(), name='review-create'),
    path('update/<int:pk>/', views.ReviewUpdateView.as_view(), name='review-update'),
    #path('delete/<int:pk>/', views.ReviewDeleteView.as_view(), name='review-delete'),
    path('user/', views.UserReviewListView.as_view(),name='user-review-list'),
]