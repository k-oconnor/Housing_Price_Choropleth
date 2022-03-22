"""Takes county-level dataframes and merges the appropriate FIPS codes to each county.  This
will then be used to generate county-level choropleths"""

# import modules
import csv
import os
import pandas as pd

# set paths and directories
IN_PATH = os.path.join("data", "US_FIPS_Codes.csv")
IN_PATH_2 = os.path.join("data", "COUNTY_YEARLY.csv")
IN_PATH_AG = os.path.join("data", "COUNTY_AGGREGATE.csv")
OUTPUT_DIR = "data"
FINAL_MERGE_PATH = os.path.join(OUTPUT_DIR, "CTY_Fips_Merge.csv")
FINAL_MERGE_PATH_AG = os.path.join(OUTPUT_DIR, "COUNTY_AGGREGATE_FIPS.csv")

# takes original data frames and saves them into objects
county_raw = pd.read_csv(IN_PATH_2)
county_ag = pd.read_csv(IN_PATH_AG)

# creates a dictionary mapping the appropriate FIPS code to each county
fips_dict = {}
with open(IN_PATH) as in_file:
    reader = csv.DictReader(in_file)
    for row in reader:
        if row["State"] == "Louisiana":
            a = (row["State"], row["County Name"] + " Parish")
            b = row["FIPS State"]
            c = row["FIPS County"]
            if a not in fips_dict and row["County Name"] != "NA":
                fips_dict[a] = b + c
        else:
            a = (row["State"], row["County Name"] + " County")
            b = row["FIPS State"]
            c = row["FIPS County"]
            if a not in fips_dict and row["County Name"] != "NA":
                fips_dict[a] = b + c

# Making the dictionary into a list
keys = list(fips_dict.keys())
values = list(fips_dict.values())

key_list = []

for i in range(len(keys)):
    key_list += [list(keys[i]) + [values[i]]]

# Making list into a dataframe
key_frame = pd.DataFrame(key_list, columns=["STNAME", "CTYNAME", "FIPS"])

# print(key_frame[key_frame["STNAME"] == "Louisiana"])

# Merges dataframes into final product to be saved into CSVs.
county_merge = pd.merge(key_frame, county_raw, on=["STNAME", "CTYNAME"])
county_merge_ag = pd.merge(key_frame, county_ag, on=["STNAME", "CTYNAME"])

# save to CSVs
county_merge.to_csv(FINAL_MERGE_PATH)
county_merge_ag.to_csv(FINAL_MERGE_PATH_AG)
