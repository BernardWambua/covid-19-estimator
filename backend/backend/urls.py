from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend_estimator_api.views import Estimator

urlpatterns = [
    path('api/v1/on-covid-19/', Estimator.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
