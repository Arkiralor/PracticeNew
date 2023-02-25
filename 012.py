import requests

GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

params = {
    'address': 'London, United Kingdom',
    'sensor': 'false',
    'region': 'uk',
    'key': ''
}

# Do the request and get the response data
req = requests.get(GOOGLE_MAPS_API_URL, params=params)
res = req.json()
print(res)

# Use the first result
# result = res['results'][0]

# geodata = dict()
# geodata['lat'] = result['geometry']['location']['lat']
# geodata['lng'] = result['geometry']['location']['lng']
# geodata['address'] = result['formatted_address']

# print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
# 221B Baker Street, London, Greater London NW1 6XE, UK. (lat, lng) = (51.5237038, -0.1585531)