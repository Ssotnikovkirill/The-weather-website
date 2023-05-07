from django.db.models import Prefetch
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContinentSerializer, CountrySerializer, CitySerializer, DateWeatherSerializer
from .models import Continent, Country, City, DateWeather

# Create your views here.
class ContinentListAll(APIView):
    def get(self, request, format=None):
        continents = Continent.objects.all()
        serializer = ContinentSerializer(continents, many=True)
        return Response(serializer.data)


class ContinentList(viewsets.ViewSet):
    def list(self, request, continent_name=None):
        queryset = Continent.objects.all()
        user = get_object_or_404(queryset, continent_name=continent_name)
        serializer = ContinentSerializer(user)
        return Response(serializer.data)

    def retrieve(self, request, continent_name=None, country_name=None, city_name=None):
        if country_name and city_name:

            queryset = Continent.objects.filter(continent_name=continent_name).prefetch_related(
                Prefetch("country", queryset=Country.objects.filter(
                    country_name=country_name).prefetch_related(
                    Prefetch('city', queryset=City.objects.filter(city_name=city_name)))
                )
            )
        else:
            queryset = Continent.objects.filter(continent_name=continent_name).prefetch_related(
                Prefetch("country", queryset=Country.objects.filter(
                    country_name=country_name))
            )

        serializer = ContinentSerializer(queryset, many=True)

        return Response(serializer.data)

class CountryList(APIView):
    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class CityList(APIView):
    def get(self, request, format=None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


class DateWeatherList(APIView):
    def get(self, request, format=None):
        dateweathers = DateWeather.objects.all()
        serializer = DateWeatherSerializer(dateweathers, many=True)
        return Response(serializer.data)


def index(request):
    return render(request, 'index.html')