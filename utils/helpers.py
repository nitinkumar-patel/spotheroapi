from parkspot.models import RateInfo
import arrow
from arrow import Arrow
from typing import List
from django.db.models.query import QuerySet


def get_time(utc_date: Arrow) -> str:
    hour: int = utc_date.hour
    minute: int = utc_date.minute
    return f'{hour:02d}{minute:02d}'


def is_date_in_range(start_date: str, end_date: str, rate: RateInfo) -> bool:

    utc_start_date: Arrow = arrow.get(start_date).to(rate.tz)
    utc_end_date: Arrow = arrow.get(end_date).to(rate.tz)

    # print(f'utc_start_date:{utc_start_date}, utc_end_date:{utc_end_date}')

    # date should not be equal
    if str(utc_start_date.date()) != str(utc_end_date.date()):
        return False

    # day's first three chars should be in rate days
    if utc_start_date.format("ddd").lower() not in rate.days.lower():
        return False

    # trim time form datetime (arrow) object
    start_time = int(get_time(utc_start_date))
    end_time = int(get_time(utc_end_date))

    # start time should not be grater than end time
    if start_time >= end_time:
        return False

    # split range time (start, end) from rate times
    range_start, range_end = tuple(rate.times.split('-'))

    # start and end time should be in range
    return int(range_start) <= start_time and end_time <= int(range_end)


def find_rate_by_dates(start_date: str, end_date: str, rates: QuerySet) -> List:
    # filter rate ids from given rates if the start and end dates are valid (in date range)
    return [rate.id for rate in rates if is_date_in_range(start_date, end_date, rate)]
