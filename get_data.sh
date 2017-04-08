#!/bin/bash

wget http://trafiopendata.97.fi/opendata/Veneet_1_7.zip
unzip Veneet_1_7.zip
rm Veneet_1_7.zip
mkdir data
mv avoindata1_7.csv data/data.csv
