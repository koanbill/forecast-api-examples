import os
import configparser

# Get API Key
api_key = os.getenv("METAPIKEY")
if not api_key:
    raise ValueError("API key not found. Make sure you have set the METAPIKEY environment variable.")

# Read coordinates from the config file
config = configparser.ConfigParser()
config.read('config.ini')

lon = float(config.get('Location', 'lon'))
lat = float(config.get('Location', 'lat'))

