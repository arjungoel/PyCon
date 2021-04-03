import requests


def get_forecasts(city):
    weather = requests.get(
        f"https://worldweather.wmo.int/en/json/{city}_en.json").json()
    print(weather)
