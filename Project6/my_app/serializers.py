from rest_framework import serializers
from .models import *

class DateWeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = DateWeather
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    dateweather = DateWeatherSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    city = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = '__all__'


class ContinentSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True, read_only=True)

    class Meta:
        model = Continent
        fields = '__all__'









