from django.db import models

# Create your models here.


class Continent(models.Model):
    continent_name = models.CharField(max_length=100, unique=True, help_text="Enter the name of continent")
    continent_img = models.TextField(max_length=1000000, blank=True)

    def __str__(self):
        return self.continent_name


class Country(models.Model):
    continent = models.ForeignKey(
        Continent, on_delete=models.CASCADE, related_name="country")
    country_name = models.CharField(max_length=255, unique=True)
    flag = models.CharField(max_length=1000000, blank=True)

    def __str__(self):
        return self.country_name


class City(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="city")
    city_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.city_name


class DateWeather(models.Model):
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="dateweather")
    date = models.DateField()
    weather_status = models.CharField(max_length=255)
    status_icon = models.CharField(max_length=1000000, blank=True)
    wind_speed = models.IntegerField(help_text="Enter the wind speed value in km/h.")
    humidity = models.IntegerField(help_text="Enter humidity value in percent(%).")
    temperature = models.IntegerField(help_text="Enter temperature value in degrees.")

    def __str__(self):
        return str(self.city)
