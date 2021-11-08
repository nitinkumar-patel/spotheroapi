import pytest
import arrow
from model_bakery import baker

from utils.helpers import get_time, is_date_in_range, find_rate_by_dates
from parkspot.models import RateInfo

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    'date, expected',
    [
        ('2015-07-01T07:00:00-05:00', '0700'),
        ('2015-07-04T15:00:00+00:00', '1000'),
        ('2015-07-04T07:30:00+05:00', '2130'),
        ('2015-07-04T07:30:00-05:00', '0730'),
        ('2015-07-04T07:30:00-06:00', '0830'),
    ],
)
def test_get_time(date, expected):

    utc_date = arrow.get(date).to('America/Chicago')

    assert get_time(utc_date) == expected


@pytest.mark.parametrize(
    'start, end, rate, expected',
    [
        (
            '2015-07-01T07:00:00-05:00',
            '2015-07-01T12:00:00-05:00',
            {"days": "wed", "times": "0600-1800", "tz": "America/Chicago", "price": 1750},
            True,
        ),
        (
            '2015-07-02T07:00:00-05:00',
            '2015-07-02T12:00:00-05:00',
            {"days": "wed", "times": "0600-1800", "tz": "America/Chicago", "price": 1750},
            False,
        ),
        (
            '2015-07-02T07:00:00-05:00',
            '2015-07-01T12:00:00-05:00',
            {"days": "wed", "times": "0600-1800", "tz": "America/Chicago", "price": 1750},
            False,
        ),
        (
            '2015-07-04T15:00:00+00:00',
            '2015-07-04T20:00:00+00:00',
            {"days": "fri,sat,sun", "times": "0900-2100", "tz": "America/Chicago", "price": 2000},
            True,
        ),
        (
            '2015-07-04T15:00:00+00:00',
            '2015-07-05T20:00:00+00:00',
            {"days": "fri,sat,sun", "times": "0900-2100", "tz": "America/Chicago", "price": 2000},
            False,
        ),
        (
            '2015-07-04T07:00:00+05:00',
            '2015-07-04T20:00:00+05:00',
            {"days": "wed", "times": "0600-1800", "tz": "America/Chicago", "price": 1750},
            False,
        ),
    ],
)
def test_is_date_in_range(start, end, rate, expected):
    assert is_date_in_range(start, end, RateInfo(**rate)) == expected


@pytest.mark.parametrize(
    'start, end, return_value',
    [
        ('2015-07-01T07:00:00-05:00', '2015-07-01T12:00:00-05:00', True),
        ('2015-07-04T15:00:00+00:00', '2015-07-04T20:00:00+00:00', False),
        ('2015-07-04T07:00:00+05:00', '2015-07-04T20:00:00+05:00', False),
    ],
)
def xtest_find_rate_by_dates(start, end, return_value, mocker):
    rate = baker.make(RateInfo)
    rate_dict = {"days": "wed", "times": "0600-1800", "tz": "America/Chicago", "price": 1750}
    expected = [rate.id]

    mocker.patch('helpers.is_date_in_range', return_value=return_value)

    assert find_rate_by_dates(start, end, [RateInfo(**rate_dict)]) == expected
