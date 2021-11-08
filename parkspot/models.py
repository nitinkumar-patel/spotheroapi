from django.db import models


class RateInfo(models.Model):
    id = models.AutoField(primary_key=True)
    days = models.TextField(
        db_column='days', blank=True, null=True
    )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    times = models.TextField(db_column='times', blank=True, null=True)  # Field name made lowercase.
    tz = models.TextField(db_column='tz', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='price', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'RateInfo'
