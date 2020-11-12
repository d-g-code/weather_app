import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import City
from .form import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=9f8d43be5018fdd74f77be99d870cecb'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        return HttpResponseRedirect('')

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    return render(request, 'weather/index.html', {'weather_data': weather_data, 'form': form})
