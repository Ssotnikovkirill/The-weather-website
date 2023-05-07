from django.contrib import admin
from my_app.models import *

# Register your models here.
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(City)


@admin.register(DateWeather)
class DateWeatherAdmin(admin.ModelAdmin):
    list_display = ['city', 'date']
