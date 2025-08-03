from django.urls import path
from .views import trainModel, getRecommendedNews  # Import the view
from .auth_views import SignupAPIView

urlpatterns = [
    path('train/', trainModel, name='train_model'),  # Register the URL path 'train/' with the trainModel view
    path('get_news/', getRecommendedNews, name='get_news'),
    path('signup/', SignupAPIView.as_view(), name='signup'),
]
