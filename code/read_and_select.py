'''A script that reads in the realestate and census data sets,
    and selects the appropriate columns for later merging'''

import csv
import os
import re
import numpy as np
import pandas as pd
# cd into the project repo for the relative paths to work. For example:
# cd /Users/amalkadri/Documents/GitHub/Python_Econ395m/eco395m-homework-6/
IN_PATH = os.path.join("data", "2010-2019-Census-Data-raw.csv")
OUTPUT_DIR = "artifacts"
FINAL_HOUSE_PATH = os.path.join(OUTPUT_DIR, "zillow_clean.csv")
FINAL_CENSUS_PATH = os.path.join(OUTPUT_DIR, "census_clean.csv")

'''make sure to do some preliminary checking to make sure the county names match and are the same object time to make merging easier'''

census_data_raw = pd.read_csv(IN_PATH, encoding = 'latin-1')

IN_PATH = os.path.join("data", "County_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")
county_time_raw = pd.read_csv(IN_PATH)

#check missing in each column
census_data_raw.isna().sum() #no missing value
county_time_raw.isna().sum()

#replace missing values with 0
county_time_raw[['1/31/2000', '2/29/2000', '3/31/2000', '4/30/2000', '9/30/2021', '10/31/2021', '11/30/2021']] = county_time_raw[['1/31/2000', '2/29/2000', '3/31/2000', '4/30/2000', '9/30/2021', '10/31/2021', '11/30/2021']].fillna(value = 0)

#Dictionary of full state names and abbreviations
state_to_abb = {
    # Other
    'District of Columbia': 'DC',

    # States
    'Alabama': 'AL',
    'Montana': 'MT',
    'Alaska': 'AK',
    'Nebraska': 'NE',
    'Arizona': 'AZ',
    'Nevada': 'NV',
    'Arkansas': 'AR',
    'New Hampshire': 'NH',
    'California': 'CA',
    'New Jersey': 'NJ',
    'Colorado': 'CO',
    'New Mexico': 'NM',
    'Connecticut': 'CT',
    'New York': 'NY',
    'Delaware': 'DE',
    'North Carolina': 'NC',
    'Florida': 'FL',
    'North Dakota': 'ND',
    'Georgia': 'GA',
    'Ohio': 'OH',
    'Hawaii': 'HI',
    'Oklahoma': 'OK',
    'Idaho': 'ID',
    'Oregon': 'OR',
    'Illinois': 'IL',
    'Pennsylvania': 'PA',
    'Indiana': 'IN',
    'Rhode Island': 'RI',
    'Iowa': 'IA',
    'South Carolina': 'SC',
    'Kansas': 'KS',
    'South Dakota': 'SD',
    'Kentucky': 'KY',
    'Tennessee': 'TN',
    'Louisiana': 'LA',
    'Texas': 'TX',
    'Maine': 'ME',
    'Utah': 'UT',
    'Maryland': 'MD',
    'Vermont': 'VT',
    'Massachusetts': 'MA',
    'Virginia': 'VA',
    'Michigan': 'MI',
    'Washington': 'WA',
    'Minnesota': 'MN',
    'West Virginia': 'WV',
    'Mississippi': 'MS',
    'Wisconsin': 'WI',
    'Missouri': 'MO',
    'Wyoming': 'WY',
}

state_abb = []
for state in census_data_raw['STNAME']: 
    if state in state_to_abb.keys(): 
        state_abb.append(state_to_abb[state]) #append the abbriviation

census_data_raw['STABB'] = state_abb

val_list = list(state_to_abb.values()) # list of abbreviations
key_list = list(state_to_abb.keys()) # list of full name

state_names = []
for abb in county_time_raw['State']:
    if abb in val_list:
        position = val_list.index(abb)
        state_names.append(key_list[position]) 

county_time_raw['STNAME'] = state_names

#select state names column and the data columns
house_prices = county_time_raw[['STNAME']].join(county_time_raw.loc[:,['/' in i for i in county_time_raw.columns]])

#group all counties by states and calculate mean for each columns
house_prices = house_prices.groupby('STNAME').mean()

#add percentage change column
house_prices['change'] = (house_prices['1/31/2022'] / house_prices['1/31/2000']) * 100


print(house_prices)


