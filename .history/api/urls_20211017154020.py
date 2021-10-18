from django.urls import path
from .views import ReturnsPrediction

urlpatterns = [
    path('returns/', ReturnsPrediction.as_view(), name = 'returns_prediction'),
]