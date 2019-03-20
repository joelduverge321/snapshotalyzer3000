import requests

requests.get('http://nasa.gov')

resp = requests.get('http://nasa.gov')
#to make sure the site is responsive
resp.status_code
#to see the data in text
resp.text
#to see the length of the text
len(resp.text)

#Getting the data
meteor_resp = requests.get('https://data.nasa.gov/resource/y77d-th95.json')
#to make sure the site is responsive
meter_resp.status_code
#to see the data in text
meteor_resp.text

meteor_resp.json()

meteor_data = meteor_resp.json()
#to know whats the type of data
type(meteor_data)

for meteor in meteor_data: print(type(meteor))
#to look at the first set of data
meteor_data[0]

#this math is helpful
import math

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

meteor_data[0]

calc_dist(50.775000, 6.083330, 29.424122, -98.493628)
#my_loc - San Antonio
my_loc = (29.424122, -98.493628)

float(meteor_data[0]['reclat'])

for meteor in meteor_data:
    if not ('reclat' in meteor and 'reclong' in meteor): continue
    meteor['distance'] = calc_dist(float(meteor['reclat']), float(meteor['reclong']), my_loc[0], my_loc[1])

meteor_data[0]

def get_dist(meteor):
    return meteor.get('distance', math.inf)

meteor_data.sort(key=get_dist)

meteor_data[0:10]

#
meteor_data[-1:-11:-1]
#total of all data/meteors
len(meteor_data)
#total meteors that do not have location data
len([m for m in meteor_data if 'distance' not in m])

