'''Determine the percentage in housing pricesincrease for 
    each year for each county. Turn that data frame into a
    csv. Then aggregate the data into state level averages,
    and generate a csv for that state-level data set as well.'''

import csv
import os
import re
import numpy as np
import pandas as pd
# cd into the project repo for the relative paths to work. For example:
# cd /Users/amalkadri/Documents/GitHub/Housing_Price_Chloropleth/
IN_PATH = os.path.join("data", "zillow_census_clean.csv")
OUTPUT_DIR = "data"
COUNTY_OUT_PATH = os.path.join(OUTPUT_DIR, "zillow_counties_final.csv")
STATE_OUT_PATH = os.path.join(OUTPUT_DIR, "zillow_states_final.csv")

#read in data
clean_data = pd.read_csv(IN_PATH)
clean_data = clean_data[['STNAME', 'CTYNAME', 'PRICE', 'YEAR', 
    'POPULATION', 'STATEPOP', 'POPWEIGHT', 'W_PRICE']]

#aggregate state level data
state_agg = clean_data.groupby(['STNAME', 'YEAR'])['W_PRICE'].sum().to_frame().reset_index()

#create cleaner county-level data
county_agg = clean_data[['STNAME', 'CTYNAME', 'PRICE', 'YEAR', 
    'POPULATION', 'STATEPOP']]
