import urllib.request
import json

def print_results(data):
    json_data = json.loads(data)
    if 'title' in json_data['metadata']:
        print(json_data['metadata']['title'])
        
    count = json_data['metadata']['count']
    print(str(count), 'earthquakes')
    
    for i in json_data['features']:
        mag = i['properties']['mag']
        if mag >= 4.0:
            print('%2.1f' % mag, i['properties']['place'])

def earthquake():
    url_data = r'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson'
    web_url = urllib.request.urlopen(url_data)
    print('HTTP code:', str(web_url.getcode()))
    if (web_url.getcode() == 200):
        data = web_url.read()
        print_results(data)
    else:
        print('error')
        
earthquake()