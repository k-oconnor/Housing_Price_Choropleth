import os
import pandas as pd

IN_PATH = os.path.join("Data", "US_FIPS_Codes.csv")
IN_PATH_AV = os.path.join("Data", "STATE_PRICE_AV.csv")
IN_PATH_AGG = os.path.join("Data", "STATE_AGGREGATE.csv")
OUTPUT_DIR = "Data"
FINAL_MERGE_PATH_AV = os.path.join(OUTPUT_DIR, "ST_yoy_avg_fips_Merge.csv")
FINAL_MERGE_PATH_AGG = os.path.join(OUTPUT_DIR, "ST_Agg_Fips_Merge.csv")

state_raw_av = pd.read_csv(IN_PATH_AV)
state_raw_agg = pd.read_csv(IN_PATH_AGG)

fips_dict = {
    "Alabama": "01",
    "Montana": "30",
    "Alaska": "02",
    "Nebraska": "31",
    "Arizona": "04",
    "Nevada": "32",
    "Arkansas": "05",
    "New Hampshire": "33",
    "California": "06",
    "New Jersey": "34",
    "Colorado": "08",
    "New Mexico": "35",
    "Connecticut": "09",
    "New York": "36",
    "Delaware": "10",
    "North Carolina": "37",
    "Florida": "12",
    "North Dakota": "38",
    "Georgia": "13",
    "Ohio": "39",
    "Hawaii": "15",
    "Oklahoma": "40",
    "Idaho": "16",
    "Oregon": "41",
    "Illinois": "17",
    "Pennsylvania": "42",
    "Indiana": "18",
    "Rhode Island": "44",
    "Iowa": "19",
    "South Carolina": "45",
    "Kansas": "20",
    "South Dakota": "46",
    "Kentucky": "21",
    "Tennessee": "47",
    "Louisiana": "22",
    "Texas": "48",
    "Maine": "23",
    "Utah": "49",
    "Maryland": "24",
    "Vermont": "50",
    "Massachusetts": "25",
    "Virginia": "51",
    "Michigan": "26",
    "Washington": "53",
    "Minnesota": "27",
    "West Virginia": "54",
    "Mississippi": "28",
    "Wisconsin": "55",
    "Missouri": "29",
    "Wyoming": "56",
}


state_raw_agg["FIPS"] = state_raw_agg["STNAME"].map(fips_dict)
state_raw_agg.to_csv(FINAL_MERGE_PATH_AGG)

state_raw_av["FIPS"] = state_raw_av["STNAME"].map(fips_dict)
state_raw_av.to_csv(FINAL_MERGE_PATH_AV)
