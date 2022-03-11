'''A script that reads in the realestate and census data sets,
    and selects the appropriate columns for later merging'''

import csv
import os
# cd into the project repo for the relative paths to work. For example:
# cd /Users/amalkadri/Documents/GitHub/Python_Econ395m/eco395m-homework-6/
IN_PATH = os.path.join("data", "2010-2019-Census-Data-raw.csv")
OUTPUT_DIR = "artifacts"
FINAL_HOUSE_PATH = os.path.join(OUTPUT_DIR, "zillow_clean.csv")
FINAL_CENSUS_PATH = os.path.join(OUTPUT_DIR, "census_clean.csv")

'''make sure to do some preliminary checking to make sure the county names match and are the same object time to make merging easier'''