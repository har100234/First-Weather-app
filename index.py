from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def get_weather(city):
    api_key = 'ead60c8959ac4900f01b45f8bebd82e4'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_weather', methods=['POST'])
def get_weather_data():
    city = request.form['city']
    if not city:
        return 'Please enter a city name.'

    try:
        weather_data = get_weather(city)
        return render_template('weather_data.html', data=weather_data)
    except Exception as e:
        return f'Error fetching weather data: {e}'


if __name__ == '__main__':
    app.run(debug=True)
