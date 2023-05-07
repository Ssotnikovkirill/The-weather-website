"""Project6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('', views.index, name='index'),

    path("admin/", admin.site.urls),

    path('continentsAll/', views.ContinentListAll.as_view()),

    path('continents/<str:continent_name>/',
         views.ContinentList.as_view({'get': 'list'})),

    path('continents/<str:continent_name>/<str:country_name>/<str:city_name>',
         views.ContinentList.as_view({'get': 'retrieve'})),

    path('countries/', views.CountryList.as_view()),
    path('cities/', views.CityList.as_view()),
    path('weather/', views.DateWeatherList.as_view()),
    # path('', views.home, name="home"),
    # path('continents/', views.get_continent, name="get_continent")
]
