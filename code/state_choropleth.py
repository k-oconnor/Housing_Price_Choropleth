import csv
import os
import re
import numpy as np
import pandas as pd
import plotly.express as px
import json

IN_PATH = os.path.join("data", "US_FIPS_Codes.csv")
IN_PATH_2 = os.path.join("data", "STATE_YEARLY.csv")
OUTPUT_DIR = "Data"
FINAL_MERGE_PATH = os.path.join(OUTPUT_DIR, "ST_Fips_Merge.csv")

state_raw = pd.read_csv(IN_PATH_2)

fips_dict = {}
with open (IN_PATH) as in_file:
    reader = csv.Dictreader(in_file)
    for row in reader:
        a = row['State']
        b = row['FIPS State']
        if a in fips_dict and row['State'] != 'NA':
            pass
        else:
            try:
                fips_dict[a] = b
            except:
                pass

state_raw['FIPS'] = state_raw['STNAME'].map(fips_dict)
state_raw.to_csv(FINAL_MERGE_PATH)
