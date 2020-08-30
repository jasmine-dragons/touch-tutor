from ipstack import GeoLookup
import os
from dotenv import load_dotenv

load_dotenv()
GEO_API = os.getenv('GEOAPI')

geo_lookup = GeoLookup(GEO_API)
geo_lookup = GeoLookup('.....')
location = geo_lookup.get_location('github.com')
print(location)
