#!/bin/sh

if [ ! -e raw.json ]; then
  ./download.pl

  ogr2ogr -q -f GeoJSON raw.json raw.osm multipolygons 2>&1 \
    | grep -v 'random layer reading'
fi

./process.py

SCALE=3

ogr2ogr -q -simplify $(echo "10^-$SCALE" | bc -l) -f GeoJSON \
  "../pub/eu-$SCALE.json" processed.json multipolygons 2>&1 \
  | grep -v 'random layer reading'
