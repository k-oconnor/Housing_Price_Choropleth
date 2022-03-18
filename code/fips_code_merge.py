import csv
import os
import re
import numpy as np
import pandas as pd
import plotly.express as px


IN_PATH = os.path.join("Data", "US_FIPS_Codes.csv")
IN_PATH_2 = os.path.join("Data", "COUNTY_YEARLY.csv")
OUTPUT_DIR = "Data"
FINAL_MERGE_PATH = os.path.join(OUTPUT_DIR, "Fips_Merge.csv")

county_raw = pd.read_csv(IN_PATH_2)

fips_dict = {}
with open (IN_PATH) as in_file:
    reader = csv.DictReader(in_file)
    for row in reader:
        a = row['County Name'] + " County"
        b = row['FIPS State']
        c = row['FIPS County']
        if a in fips_dict and row['County Name'] != 'NA':
            pass
        else:
            try:
                fips_dict[a] = (b + c)
            except:
                pass

county_raw['FIPS'] = county_raw['CTYNAME'].map(fips_dict)
county_raw.to_csv(FINAL_MERGE_PATH)
