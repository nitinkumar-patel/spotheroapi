from rest_framework import generics

from .models import RateInfo
from .serializers import RateInfoSerializer


class RateInfoList(generics.ListCreateAPIView):
    queryset = RateInfo.objects.all()
    serializer_class = RateInfoSerializer


class RateInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RateInfo.objects.all()
    serializer_class = RateInfoSerializer
