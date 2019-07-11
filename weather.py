import os
import json
import requests

from datetime import datetime


def get_weather():
    key = os.environ["darksky_token"]
    base_url = "https://api.darksky.net"
    # Utrecht coordinates
    lat = 52.099662
    lon = 5.103362
    url = f"{base_url}/forecast/{key}/{lat},{lon}?units=si"
    r = json.loads(requests.get(url).text)

    return (
        r["daily"]["data"][0]["summary"],
        r["daily"]["data"][0]["temperatureHigh"],
        r["daily"]["data"][0]["temperatureLow"],
    )
