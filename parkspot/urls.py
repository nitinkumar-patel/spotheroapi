from rest_framework.urlpatterns import format_suffix_patterns
from parkspot import views
from django.urls import path

urlpatterns = [
    path('', views.RateInfoList.as_view(), name='rates-info-list'),
    path('<int:pk>/', views.RateInfoDetail.as_view(), name='rates-info-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
