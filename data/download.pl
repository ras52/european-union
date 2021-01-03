#!/usr/bin/perl

my @rels = (
  52411,   # Belgium
  2171347, # Luxembourg

  47796,   # Netherlands including Caribbean Netherlands
  1216720, # Caribbean Netherlands (Bonaire, Saba, Sint Eustatius)

  51477,   # Germany

  51529,   # Schleswig-Holstein  \\ Start of West Germany, in 1949
  62782,   # Hamburg
  62771,   # Lower Saxony
  62718,   # Bremen
  62761,   # North Rhine-Westphalia
  62650,   # Hesse
  62341,   # Rhineland-Palatinate
  62611,   # Baden-Wurttemberg
  2145268, # Bavaria             // End of West Germany, in 1949
  62372,   # Saarland

  16343,   # Spandau             \\ Modern boroughs wholly in West Berlin
  404538,  # Charlottenburg-Wilmersdorf 
  16334,   # Reinickendorf
  55734,   # Steglitz-Zehlendorf 
  158437,  # Tempelhof-Schöneberg
  162902,  # Neukölln            //

  55750,   # Tiergarten          \\ Localities (/Ortsteile/) in West Berlin
  16567,   # Hansaviertel         | The former borough of Tiergarten
  28339,   # Moabit              // 
  28267,   # Wedding             \\ The former borough of Weddding
  28426,   # Gesundbrunnen       //
  55765,   # Kreuzberg           }} The former borough of Kreuzberg

  365331,  # Italy
  179292,  # Trieste

  1403916, # Metropolitan France
  192756,  # Algeria
  1785276, # Reunion
  1260551, # French Guiana
  1891495, # Martinique
  1401835, # Guadeloupe
  1891583, # Saint Martin
  537967,  # Saint Barthelemy

  50046,   # Denmark
  2184073, # Greenland
  62273,   # Ireland
  62149,   # United Kingdom 
  1278736, # Gibraltar
  192307,  # Greece
  295480,  # Portugal
  1311341, # Spain
  16239,   # Austria
  52822,   # Sweden
  54224,   # Finland

  365307,  # Malta
  3263726, # Cyprus
  79510,   # Estonia
  72594,   # Latvia
  72596,   # Lithuania
  49715,   # Poland
  51684,   # Czechia
  14296,   # Slovakia
  21335,   # Hungary
  218657,  # Slovenia

  90689,   # Romania 
  186382,  # Bulgaria
  214885,  # Croatia
);

$rels = join ',', @rels;
system 'curl', '-s', '-o', "raw.osm", '-d', "rel(id:$rels);(._;>;);out;",
  'https://overpass-api.de/api/interpreter';
