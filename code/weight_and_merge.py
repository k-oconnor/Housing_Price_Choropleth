'''Apply population weighting to all counties and merge weight score
    with cleaned zillow data set, then create merged data frame.
    Then generate weighted average housing prices for later analysis'''

import csv
import os
# cd into the project repo for the relative paths to work. For example:
# cd /Users/amalkadri/Documents/GitHub/Housing_Price_Chloropleth/
ZILLOW_IN_PATH = os.path.join("artifacts", "zillow_clean.csv")
CENSUS_IN_PATH = os.path.join("artifacts", "census_clean.csv")
OUTPUT_DIR = "artifacts"
OUT_PATH = os.path.join(OUTPUT_DIR, "zillow_merged.csv")
