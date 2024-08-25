from django.db import models

# Create your models here.


class RealEstateAveragePrice(models.Model):
    date = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    city_name = models.CharField(max_length=50, blank=True, null=True)
    real_estate_type = models.CharField(max_length=50, blank=True, null=True)
    market_type = models.CharField(max_length=50, blank=True, null=True)
    total_price = models.IntegerField()
    m2_price = models.IntegerField()
    rooms = models.FloatField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    samples = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'real_estate_average_price'


class HistoricalRealEstatesPrice(models.Model):
    date = models.CharField(max_length=50, blank=True, null=True)
    city_name = models.CharField(max_length=50, blank=True, null=True)
    market_type = models.CharField(max_length=50, blank=True, null=True)
    m2_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historical_real_estates_price'