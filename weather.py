import os
import json
import requests

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

from datetime import datetime, timedelta


def get_weather(lat=52.099662, lon=5.103362):
    # Utrecht coordinates
    # lat = 52.099662
    # lon = 5.103362
    key = os.environ["darksky_token"]
    base_url = "https://api.darksky.net"
    url = f"{base_url}/forecast/{key}/{lat},{lon}?units=si"
    r = json.loads(requests.get(url).text)

    return (
        r["daily"]["data"][0]["summary"],
        r["daily"]["data"][0]["temperatureHigh"],
        r["daily"]["data"][0]["temperatureLow"],
    )


def get_radar(lat=52.099662, lon=5.103362):
    # Utrecht coordinates
    # lat = 52.099662
    # lon = 5.103362

    delta_minutes = 5
    now = datetime.now()
    base_url = "https://gpsgadget.buienradar.nl/data/raintext"
    url = f"{base_url}?lat={lat}&lon={lon}"
    text = requests.get(url).text.replace("\r", "").split("\n")
    rain = [float(i.split("|")[0]) / 100 for i in text[:-1]]
    date_zero = f'{now.strftime("%Y/%m/%d")} {text[0].split("|")[1]}'
    times = [
        datetime.strptime(date_zero, "%Y/%m/%d %H:%M") + timedelta(minutes=i * 5)
        for i in range(len(text[:-1]))
    ]

    myFmt = DateFormatter("%H:%M")
    fig, ax = plt.subplots()
    ax.plot(times, rain)
    ax.fill_between(times, 0, rain)
    ax.xaxis.set_major_formatter(myFmt)
    ax.set_ylim(0, 6)
    ax.axhline(y=2, linestyle="--", color="black", lw=1)
    ax.axhline(y=4, linestyle="--", color="black", lw=1)
    ax.text(times[-3], 1, "light")
    ax.text(times[-3], 3, "medium")
    ax.text(times[-3], 5, "heavy")
    ax.set_title(f'Utrecht {now.strftime("%d %B %Y")}')
    fig.autofmt_xdate()
    fn = f"./media/radar_{now.isoformat()}.png"
    plt.savefig(fn)

    return fn
