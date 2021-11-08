from rest_framework import viewsets
from rest_framework.response import Response

from parkspot.models import RateInfo
from .serializers import PriceInfoSerializer
from utils import helpers
from rest_framework.filters import BaseFilterBackend
import coreapi


# ref: https://newbedev.com/how-to-show-query-parameter-options-in-django-rest-framework-swagger
class SimpleFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
            coreapi.Field(name='start', location='query', required=True, type='string'),
            coreapi.Field(name='end', location='query', required=True, type='string'),
        ]


class PriceViewSet(viewsets.ViewSet):
    filter_backends = (SimpleFilterBackend,)

    def list(self, request):
        queryset = RateInfo.objects.all()

        start_date = request.GET.get('start').replace(' ', '+')
        end_date = request.GET.get('end').replace(' ', '+')

        parkspots = queryset.filter(id__in=helpers.find_rate_by_dates(start_date, end_date, queryset))

        serializer = PriceInfoSerializer(parkspots, many=True)

        json = {'price': serializer.data[0].get('price') if serializer.data else 'unavailable'}

        return Response(json)
