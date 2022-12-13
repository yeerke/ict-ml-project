from django.db import models

class Advertising(models.Model):
    daily_time_spent_on_site = models.FloatField()
    age = models.IntegerField()
    area_income = models.FloatField()
    daily_internet_usage = models.FloatField()
    ad_topic_line = models.TextField()
    city = models.TextField()
    male = models.BooleanField()
    country = models.TextField()
    timestamp = models.DateTimeField()
    clicked_on_ad = models.BooleanField()
