# parse data from raw KML files, save as geojson for d3
import json
import os
from BeautifulSoup import BeautifulSoup

RAW_DIR = 'raw/'
geojson = {'type': 'FeatureCollection', 'features': []}
for kml in os.listdir(RAW_DIR):
    with open(RAW_DIR+kml) as inKML:
        soup = BeautifulSoup(inKML.read())
        for placemark in soup.findAll('placemark'):
            properties = json.loads(placemark.description.text)
            raw_coordinates = placemark.coordinates.text
            lng,lat = raw_coordinates.split(',')
            feature = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [float(lng),float(lat)]
                },
                'properties': properties
            }
            geojson['features'].append(feature)
print json.dumps(geojson)