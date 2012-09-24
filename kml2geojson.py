# parse data from raw KML files, save as geojson for d3
import json
import os
from BeautifulSoup import BeautifulSoup

RAW_DIR = 'raw/'
geojson = {'type': 'FeatureCollection', 'features': []}
for kml in os.listdir(RAW_DIR):
    with open(RAW_DIR+kml) as inKML:
        soup = BeautifulSoup(inKML.read())
        for raw_coordinates in soup.findAll('coordinates'):
            lng,lat = raw_coordinates.text.split(',')
            feature = {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [float(lng),float(lat)]
                },
                'properties': {}    # add properties from the KML file
                                    # relevant to viz: population, id
            }
            geojson['features'].append(feature)
print json.dumps(geojson)