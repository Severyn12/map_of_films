'''
In this module were implemented some functions(file reader,
map creator,coordinates searcher). The main task of this module
is to create a map.
'''

from itertools import islice
from random import random,choice
from geopy.extra.rate_limiter import RateLimiter
from haversine import haversine
from geopy.geocoders import Nominatim
import folium
from geopy.exc import GeocoderUnavailable


geolocator = Nominatim(user_agent="two.py")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.1)

def cords(loc:str) -> tuple:
    '''
    Calculates coordinates of the place. If it's
    imposible to do, returns None.
    >>> cords('Los Angeles, California, USA)
    '''
    mist = random()
    if loc.count(',') > 1:
        split_loc = loc.split(',')
        new_loc = ','.join(split_loc[len(split_loc)-3:
        len(split_loc)])
    else:
        new_loc = loc
    try:
        location = geolocator.geocode(new_loc)
        coords = (location.latitude+mist,
        location.longitude+mist)
    except GeocoderUnavailable:
        return None
    except AttributeError:
        return None
    return coords




def selector(info:str,point:tuple) -> list:
    '''
    This function connects two others(cords and reader).
    Returns a list, which contains coordinates of the place
    and distance between that place and starting place.
    '''
    cord = cords(info)
    if cord:
        return [haversine(point,cord),cord]
    return None


def reader(year:str,point:tuple,path ='locations.list') -> list:
    '''
    Reads data from the file and creates a list from it.
    '''
    names = set()
    fil = open(path,'r',encoding='ISO-8859-1')
    res = []
    for line in islice(fil, 14, None):
        line = line.strip().split('\t')
        data = line[0][:line[0].find(')')].split(' (')
        try:
            if data[1] == str(year) and (data[0] not in names):
                if line[len(line)-1][0] == '(':
                    line = line[:len(line)-1]
                loc = selector(line[len(line)-1],point)
                names.add(data[0])
                if loc:
                    res.append((data + loc))
        except IndexError:
            continue
    return res


def color_creator() -> str:
    '''
    Randomly chooses a color from the list.
    '''
    colors = ['darkpurple', 'black',
    'purple', 'white', 'darkgreen',
    'darkblue', 'lightgray', 'cadetblue', 'red']
    return choice(colors)



def population_reader(path='world.json'):
    '''
    Creates a population map layer(if the population
    of the country is bigger than some number, then the
    country is coloured in a special color).
    '''
    fg_pp = folium.FeatureGroup(name="Population")
    fg_pp.add_child(folium.GeoJson(data=open(path, 'r',
    encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor':'orange'
    if x['properties']['POP2005'] < 10000000
    else 'blue' if 10000000<=x['properties']['POP2005']<20000000
    else 'green'}))
    return fg_pp


def cords_reader(date:str,point:tuple):
    '''
    Creates a coordinates map layer and returns it.
    '''
    fg_cord = folium.FeatureGroup(name='Kosiv map')
    base = sorted(reader(date,point),key = lambda x:x[2])[:10]
    for cord in base:
        fg_cord.add_child(folium.CircleMarker(
    location=[cord[3][0],cord[3][1]],
    radius = 10,popup=cord[0],color='green',
    fill_color=color_creator(),fill_opacity=1))
    return fg_cord



def map_create(film_year:str,point:tuple):
    '''
    Creates a map, which also consist of two previous layers.
    '''
    mapa = folium.Map(location=[point[0],point[1]],zoom_start=5)
    mapa.add_child(population_reader())
    mapa.add_child(cords_reader(film_year,point))
    mapa.add_child(folium.Marker(location=[point[0],point[1]],
    popup="Starting position"))
    mapa.save(f'{film_year}_movie_map.html')



if __name__ == "__main__":
    while True:
        try:
            year_film = int(input('Please enter a year you \
would like to have a map for:'))
            coordinate = tuple(map(float,
            input('Please enter the starting position\
(format: lat, long):').split(', ')))
        except ValueError:
            print('Try again.(Coordinates must be separated \
by comma and space. Also year must be a number)')
            continue
        break
    print('Map is generating...\nIt can take some time. Please wait...')
    map_create(year_film,coordinate)
    print(f'Finished. Please have look at the map \
{year_film}_movies_map.html')
