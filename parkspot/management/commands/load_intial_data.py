from django.core.management.base import BaseCommand
from parkspot.models import RateInfo
import json


class Command(BaseCommand):
    help = 'Displays current time'

    def import_rate(self, data):
        days = data.get('days', None)
        times = data.get('times', None)
        tz = data.get('tz', None)
        price = data.get('price', 0)

        try:  # try and catch for saving the objects
            rate, created = RateInfo.objects.get_or_create(days=days, times=times, tz=tz, price=price)
            if created:
                rate.save()
                display_format = "\nRate, {}, has been saved."
                print(display_format.format(rate))
            else:
                print(f'already there: {data}')
        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong saving this rate: {}\n{}".format(days, str(ex))
            print(msg)

    def handle(self, *args, **kwargs):
        """
        Read Jason Data from json file and load into db
        """
        with open('rates.json', encoding='utf-8') as data_file:
            json_data = json.loads(data_file.read())
            for spot_rate in json_data.get('rates'):
                # print(spot_rate)
                self.import_rate(spot_rate)
