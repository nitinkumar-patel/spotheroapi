from rest_framework import serializers
from .models import RateInfo


class RateInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateInfo
        fields = ['days', 'times', 'tz', 'price']
