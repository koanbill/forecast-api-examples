from requests import post
from os import getenv
from datetime import datetime
import json
from config import api_key, lon, lat

# NOTE: don't for get to set "apikey" env, or the default below.
resp = post(
    "https://forecast-v2.metoceanapi.com/point/time",
    headers={"x-api-key": api_key},
    json={
        "points": [{
            "lon": lon,
            "lat": lat 
        }],
        "variables": [
            "cloud.cover"
        ],
        "time": {
            "from": "{:%Y-%m-%dT00:00:00Z}".format(datetime.utcnow()),
            "interval": "3h",
            "repeat": 2
        }
    }
)

if resp.status_code != 200:
    raise ValueError("{}: {}", resp.status_code, resp.text)

print(json.dumps(resp.json(), indent=1))
