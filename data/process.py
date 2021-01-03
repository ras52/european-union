#!/usr/bin/python
# coding=utf-8

from shapely.geometry import Polygon, MultiPolygon, asShape
from shapely.ops import unary_union, cascaded_union
from geojson import Feature
import json

def load_rels():
  j = json.load(open('raw.json'))
  
  rels = {};
  
  for i, f in enumerate(j['features']):
    props = f['properties']
    if 'osm_id' in props:
      rels[ int(props['osm_id']) ] = f

  return rels;

def feature(geom, code, name):
  props = { 'name': name, 'code': code }

  return Feature(geometry=geom, properties=props)

def subtract(rels, mainid, subid, code, name):
  main = asShape(rels[mainid]['geometry'])
  sub  = asShape(rels[subid]['geometry'])

  geom = main.difference(sub)
  return feature(geom, code, name)

def extract(rels, relid, code, name):
  geom = asShape(rels[relid]['geometry'])
  return feature(geom, code, name)

def merge(rels, relids, code, name):
  geoms = [ asShape(rels[i]['geometry']) for i in relids ]
  return feature(unary_union(geoms), code, name) 

rels = load_rels()
features = []

features.append( extract(rels, 52411, 'BE', 'Belgium') )
features.append( extract(rels, 2171347, 'LU', 'Luxembourg') )

# The Netherland without the Netherlands Caribbean
features.append( subtract(rels, 47796, 1216720, 'NL', 'Netherlands') )

# West Germany before and after the incorporation of the Saarland
features.append( merge(rels, 
  [51529, 62782, 62771, 62718, 62761, 62650, 62341, 62611, 2145268],
   'DE-1949', 'West Germany') )
features.append( extract(rels, 62372, 'DE-SL', 'Saarland') )
features.append( merge(rels, 
  [51529, 62782, 62771, 62718, 62761, 62650, 62341, 62611, 2145268, 62372],
   'DE-1957', 'West Germany') )

# West Berlin was not formally part of West Germany
features.append( merge(rels,
  [16343, 404538, 16334, 55734, 158437, 162902, 
   55750, 16567, 28339, 28267, 28426, 55765], 'DE-WB', 'West Berlin') )

features.append( extract(rels, 51477, 'DE-1990', 'Germany') );

# Italy before and after the incorporation of Trieste
# TODO: 179292 doesn't include the sea border off Trieste
features.append( subtract(rels, 365331, 179292, 'IT-1947', 'Italy') )
features.append( extract(rels, 365331, 'IT-1954', 'Italy') )

# Metropolitan France and its overseas départements
features.append( extract(rels, 1403916, 'FR', 'France') )
features.append( extract(rels, 192756, 'DZ', 'French Algeria') )
features.append( extract(rels, 1785276, 'RE', 'Reúnion') )
features.append( extract(rels, 1260551, 'GF', 'French Guiana') )
features.append( extract(rels, 1891495, 'MQ', 'Martinique') )
features.append( extract(rels, 1401835, 'GP', 'Guadeloupe') )
features.append( extract(rels, 1891583, 'MF', 'Saint Martin') )
features.append( extract(rels, 537967, 'BL', 'Saint Barthélemy') )

# Denmark with and without Greenland
features.append( merge(rels, [50046, 2184073], 'DK-1953', 'Denmark') )
features.append( extract(rels, 50046, 'DK-1979', 'Denmark') )
features.append( extract(rels, 2184073, 'GL', 'Greenland') )

features.append( extract(rels, 62273, 'IE', 'Ireland') )
features.append( extract(rels, 62149, 'GB', 'United Kingdom') )
features.append( extract(rels, 1278736, 'GI', 'Gibraltar') )
features.append( extract(rels, 192307, 'GR', 'Greece') )
features.append( extract(rels, 295480, 'PT', 'Portugal') )
features.append( extract(rels, 1311341, 'ES', 'Spain') )
features.append( extract(rels, 16239, 'AT', 'Austria') )
features.append( extract(rels, 52822, 'SE', 'Sweden') )
features.append( extract(rels, 54224, 'FI', 'Finland') )

features.append( extract(rels, 365307, 'MT', 'Malta') )
features.append( extract(rels, 3263726, 'CY', 'Cyprus') )
features.append( extract(rels, 79510, 'EE', 'Estonia') )
features.append( extract(rels, 72594, 'LV', 'Latvia') )
features.append( extract(rels, 72596, 'LT', 'Lithuania') )
features.append( extract(rels, 49715, 'PL', 'Poland') )
features.append( extract(rels, 51684, 'CZ', 'Czechia') )
features.append( extract(rels, 14296, 'SK', 'Slovakia') )
features.append( extract(rels, 21335, 'HU', 'Hungary') )
features.append( extract(rels, 218657, 'SI', 'Slovenia') )

features.append( extract(rels, 90689, 'RO', 'Romania') )
features.append( extract(rels, 186382, 'BG', 'Bulgaria') )
features.append( extract(rels, 214885, 'HR', 'Croatia') )

d = { 'type': "FeatureCollection",
      'name': "multipolygons",
      'features': features }

with open('processed.json', 'w') as out:
  json.dump(d, out)
