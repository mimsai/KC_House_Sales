import time
import geopy
import pandas               as pd
import geopandas            as gpd
import matplotlib.pyplot    as plt
import plotly_express       as px

from multiprocessing          import Pool
from geopy.geocoders          import Nominatim
from geopy.extra.rate_limiter import RateLimiter


geolocator = Nominatim (user_agent = 'geopy_house', timeout = 2000)

def get_data (x):
    
    index, row = x
    time.sleep ( 3 )
    
    rgeocode = RateLimiter (geolocator.reverse, min_delay_seconds = 0.00001)
    response = geolocator.reverse(row['query'])
    
    
    house_number   = response.raw['address']['house_number']     if 'house_number'  in response.raw['address']  else 'NA'
    road           = response.raw['address']['road']             if 'road'          in response.raw['address']  else 'NA'
    neighbourhood  = response.raw['address']['neighbourhood']    if 'neighbourhood' in response.raw['address']  else 'NA'
    city           = response.raw['address']['city']             if 'city'          in response.raw['address']  else 'NA'
    state          = response.raw['address']['state']            if 'state'         in response.raw['address']  else 'NA'
    country        = response.raw['address']['country']          if 'country'       in response.raw['address']  else 'NA'
    
    return house_number, road, neighbourhood, city, state, country
