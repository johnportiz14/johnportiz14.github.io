

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks. 
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy

import glob
import getorg
from geopy import Nominatim
import os

#  g = glob.glob("*.md")
#  g = glob.glob(os.path.join(os.getcwd(), "*.md"),recursive=True)  #[JPO] look recursively


#  geocoder = Nominatim()
geocoder = Nominatim(user_agent="website") #[JPO] needs this (could given user_agent another name...)
location_dict = {}
location = ""
permalink = ""
title = ""

# Get list of _talks subdirectories
dirs = [x[0] for x in os.walk(os.getcwd())]
g = []
for d in dirs:
    #  g.append(glob.glob(os.path.join(d, "*.md"),recursive=True)) #[JPO] look recursively
    g.extend(glob.glob(os.path.join(d, "*.md"),recursive=True)) #[JPO] look recursively

for file in g:
    with open(file, 'r') as f:
        #  # The below lines don't ignore comments
        #  lines = f.read()
        #  if lines.find('location: "') > 1:
            #  loc_start = lines.find('location: "') + 11
            #  lines_trim = lines[loc_start:]
            #  loc_end = lines_trim.find('"')
            #  location = lines_trim[:loc_end]
        #[JPO] this now ignores commented lines
        for li in f:
            if li.startswith('location: "'):
                #  loc_start = li.startswith('location: "') + 11
                loc_start = li.startswith('location: "') + 10
                lines_trim = li[loc_start:]
                loc_end = lines_trim.find('"')
                location = lines_trim[:loc_end]
                #  print('location = {}'.format(location))

        location_dict[location] = geocoder.geocode(location)
        print(location, "\n", location_dict[location])


m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="../talkmap", hashed_usernames=False)




