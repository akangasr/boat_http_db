#!/bin/bash

wget http://trafiopendata.97.fi/opendata/Veneet_1_7.zip
unzip Veneet_1_7.zip
rm Veneet_1_7.zip
mkdir -p data
iconv -f iso-8859-1 -t utf8 avoindata1_7.csv > data/data.csv
rm avoindata1_7.csv
