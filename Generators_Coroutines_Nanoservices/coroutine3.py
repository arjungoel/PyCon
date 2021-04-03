import requests


def get_forecasts():

    while city_id := (yield "Send a city number or None"):

        weather = requests.get(
            f"https://worldweather.wmo.int/en/json/{city}_en.json").json()
        for one_forecast in weather['city']['forecast']['forecastDay']:
            yield one_forecast


g = get_forecasts()

print(next(g))
print(g.send(44))
