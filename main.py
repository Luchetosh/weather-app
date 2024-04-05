import requests
from flask import Flask, render_template, request
import json


app = Flask(__name__)

api_key = 'a7ef70cdd2820aed218a6f7031672783' # Key sluzi za authentikaciju

@app.route("/", methods=['GET', 'POST']) # Kada odes na localhost:port/ - sta ce se desiti
def index():
    if request.method ==  'POST': # kata na / posaljes post request - oni sadrzavaju podatke.
        city = request.form['city'] # posto koristis html, on nadje city iz forme koju saljes preko post-a
        weather_data = get_weather(city) # preko funkcije vrati podatke
        return render_template('index.html', weather_data=weather_data) # rendera template sa podatcima
    return render_template('index.html', weather_data=None) # samo rendera template

def get_weather(city):
    try: # koristis try, ako je ikakav error imas error handling
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        weather_data = response.json()
        temperature = weather_data['main']['temp'] # ['main'] vrati sve sto je u mainu, zamisli kao samo json sa tim podatcima unutra, ['temp'] posto samo daje int (broj) mozes odma vraititi jer nedaje dalje neki json poput, prosjecna_temp, trenutni_temp itd.
        description = weather_data['weather'][0]['description']
        # [0] sluzi jer weather daje array, ili ti moze imati 10 ovih descriptiona, za mostar daje 1 ili ti nulti jer je najvr samo jedna stanicu u mostaru. ali ovo moze se koristiti ako npr grad ima vise stanica.
 	      # array exmaple = ["toni", "luka"] ....
        city_name = weather_data['name']
        country_code = weather_data['sys']['country']

        # weather_info = f'{description}, in {city_name}, {country_code}. Temperature: {temperature}C'
        weather_info = {
          'city_name': city_name,
          'description': description,
          'country_code': country_code,
          'temperature': temperature
        }
        #{description.capitalize()}, ??

        return weather_info
    except Exception as e:
        return f'Error finding weather data: {e}'
   
   
   

    
if __name__ == '__main__':
        app.run(debug=True)
