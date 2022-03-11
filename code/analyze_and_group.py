'''Determine the percentage in housing pricesincrease for 
    each year for each county. Turn that data frame into a
    csv. Then aggregate the data into state level averages,
    and generate a csv for that state-level data set as well.'''

import csv
import os
# cd into the project repo for the relative paths to work. For example:
# cd /Users/amalkadri/Documents/GitHub/Housing_Price_Chloropleth/
IN_PATH = os.path.join("artifacts", "zillow_merged.csv")
OUTPUT_DIR = "artifacts"
COUNTY_OUT_PATH = os.path.join(OUTPUT_DIR, "zillow_counties_final.csv")
STATE_OUT_PATH = os.path.join(OUTPUT_DIR, "zillow_states_final.csv")