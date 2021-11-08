from rest_framework import serializers
from parkspot.models import RateInfo


class PriceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateInfo
        fields = ['price']
