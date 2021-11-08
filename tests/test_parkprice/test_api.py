import pytest

from parkspot.models import RateInfo

pytestmark = pytest.mark.django_db

endpoint = '/prices/'


@pytest.mark.parametrize(
    'start, end, price',
    [
        ('2015-07-01T07:00:00-05:00', '2015-07-01T12:00:00-05:00', 1750),
        ('2015-07-04T15:00:00+00:00', '2015-07-04T20:00:00+00:00', 2000),
        ('2015-07-04T07:00:00+05:00', '2015-07-04T20:00:00+05:00', 'unavailable'),
    ],
)
def test_one_price_exists_should_succeed(start, end, price, rates, client) -> None:

    for data in rates:
        _ = RateInfo.objects.create(**data)

    expected_response = {'price': price}

    price_url = endpoint + f'?start={start}&end={end}'

    response = client.get(price_url)

    assert response.status_code == 200

    assert response.json() == expected_response
