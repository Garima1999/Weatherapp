from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=72a517b5751c30053b02dfb6085d6016'
	cities = City.objects.all()

	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()

	form = CityForm()
	weather_data = []

	for city in cities:

		city_weather = requests.get(url.format(city)).json()
		weather = {
		    'city' : city,
		    'temperature' : city_weather['main']['temp'],
		    'description' : city_weather['weather'][0]['description'],
		    'icon' : city_weather['weather'][0]['icon']
		}
		weather_data.append(weather)
	context = {'weather_data' : weather_data, 'form' : form}

	return render(request, "index.html",context)
