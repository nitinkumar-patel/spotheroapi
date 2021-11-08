from model_bakery import baker
import json
import pytest


from parkspot.models import RateInfo

pytestmark = pytest.mark.django_db


class TestRatesEndpoints:

    endpoint = '/rates/'

    def test_list(self, api_client):
        baker.make(RateInfo, _quantity=3)

        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_create(self, api_client):
        rate = baker.prepare(RateInfo)
        expected_json = {'days': rate.days, 'times': rate.times, 'tz': rate.tz, 'price': rate.price}

        response = api_client().post(self.endpoint, data=expected_json, format='json')

        assert response.status_code == 201
        assert json.loads(response.content) == expected_json

    def test_retrieve(self, api_client):
        rate = baker.make(RateInfo)
        expected_json = {'days': rate.days, 'times': rate.times, 'tz': rate.tz, 'price': rate.price}

        url = f'{self.endpoint}{rate.id}/'

        response = api_client().get(url)

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_update(self, api_client):
        old_rate = baker.make(RateInfo)
        new_rate = baker.prepare(RateInfo)
        rate_dict = {'days': new_rate.days, 'times': new_rate.times, 'tz': new_rate.tz, 'price': new_rate.price}

        url = f'{self.endpoint}{old_rate.id}/'

        response = api_client().put(url, rate_dict, format='json')

        assert response.status_code == 200
        assert json.loads(response.content) == rate_dict

    @pytest.mark.parametrize(
        'field',
        [
            ('days'),
            ('times'),
            ('tz'),
            ('price'),
        ],
    )
    def test_partial_update(self, field, api_client):
        rate = baker.make(RateInfo)
        rate_dict = {'days': rate.days, 'times': rate.times, 'tz': rate.tz, 'price': rate.price}
        valid_field = rate_dict[field]
        url = f'{self.endpoint}{rate.id}/'

        response = api_client().patch(url, {field: valid_field}, format='json')

        assert response.status_code == 200
        assert json.loads(response.content)[field] == valid_field

    def test_delete(self, api_client):
        rate = baker.make(RateInfo)
        url = f'{self.endpoint}{rate.id}/'

        response = api_client().delete(url)

        assert response.status_code == 204
        assert RateInfo.objects.all().count() == 0
