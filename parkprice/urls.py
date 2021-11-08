from rest_framework.urlpatterns import format_suffix_patterns
from parkprice import views
from django.urls import path

urlpatterns = [
    path('', views.PriceViewSet.as_view({'get': 'list'}), name='price-info'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
