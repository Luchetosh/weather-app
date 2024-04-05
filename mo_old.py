import requests
from flask import Flask, render_template, request, get
import json


app = Flask(__name__)

api_key = 'a7ef70cdd2820aed218a6f7031672783'

@app.route("/", methods=['GET', 'POST'])

def index():
    if request.method ==  'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        return render_template('index.html', weather_data=weather_data)
    return render_template('index.html', weather_data=None)

def get_weather(city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = request.get(url)
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        city_name = weather_data['name']
        country_code = weather_data['sys']['country']

        weather_info = f'{description.capitalize()}, in {city_name}, {country_code}. Temperature: {temperature}C'
        #{description.capitalize()}, ??

        return weather_info
    except Exception as e:
        return f'Error finding weather data: {e}'
    
    if __name__ == '__main__':
        app.run(debug=True)
