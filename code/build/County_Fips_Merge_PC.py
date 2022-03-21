import csv
import os
import pandas as pd


IN_PATH = os.path.join("Data", "US_FIPS_Codes.csv")
IN_PATH_2 = os.path.join("Data", "COUNTY_YEARLY.csv")
IN_PATH_AG = os.path.join("Data", "COUNTY_AGGREGATE.csv")
OUTPUT_DIR = "Data"
FINAL_MERGE_PATH = os.path.join(OUTPUT_DIR, "CTY_Fips_Merge.csv")
FINAL_MERGE_PATH_AG = os.path.join(OUTPUT_DIR, "COUNTY_AGGREGATE_FIPS.csv")

county_raw = pd.read_csv(IN_PATH_2)
county_ag = pd.read_csv(IN_PATH_AG)

fips_dict = {}
with open(IN_PATH) as in_file:
    reader = csv.DictReader(in_file)
    for row in reader:
        a = (row["ï»¿State"], row["County Name"] + " County")
        b = row["FIPS State"]
        c = row["FIPS County"]
        if a not in fips_dict and row["County Name"] != "NA":
            fips_dict[a] = b + c

keys = list(fips_dict.keys())
values = list(fips_dict.values())

key_list = []

for i in range(len(keys)):
    key_list += [list(keys[i]) + [values[i]]]

key_frame = pd.DataFrame(key_list, columns=["STNAME", "CTYNAME", "FIPS"])

county_merge = pd.merge(key_frame, county_raw, on=["STNAME", "CTYNAME"])

county_merge_ag = pd.merge(key_frame, county_ag, on=["STNAME", "CTYNAME"])

county_merge.to_csv(FINAL_MERGE_PATH)
county_merge_ag.to_csv(FINAL_MERGE_PATH_AG)
