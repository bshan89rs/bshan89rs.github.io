import geopandas as gpd
import os, time
import requests

api_key = r'AIzaSyBwI2pcgnIURApHk-FIdC988k_xBNG93Fw'

gdf = gpd.read_file(r"S:\OneDrive - The University of Western Ontario\Personal_Bo\Portfolio\git_site\Personal\resources\test_img.geojson")
print(gdf.head())

url = r'https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=AIzaSyBwI2pcgnIURApHk-FIdC988k_xBNG93Fw'

r = requests.post(url)
print(r)