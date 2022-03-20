# import modules
import csv
import os
import numpy as np
import pandas as pd

# cd into the project repo for the relative paths to work. For example:
# cd /Users/amalkadri/Documents/GitHub/Python_Econ395m/eco395m-homework-6/
CENSUS_IN_PATH = os.path.join("data", "2010-2019-Census-Data-raw.csv")
ZILLOW_IN_PATH = os.path.join(
    "data", "County_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"
)
OUTPUT_DIR = "data"
FINAL_PATH_CTY_TOTAL = os.path.join(OUTPUT_DIR, "COUNTY_AGGREGATE.csv")
FINAL_PATH_CTY_ANNUAL = os.path.join(OUTPUT_DIR, "COUNTY_YEARLY.csv")
FINAL_PATH_ST_AV = os.path.join(OUTPUT_DIR, "STATE_PRICE_AV.csv")
FINAL_PATH_ST_TOTAL = os.path.join(OUTPUT_DIR, "STATE_AGGREGATE.csv")
FINAL_PATH_ST_ANNUAL = os.path.join(OUTPUT_DIR, "STATE_YEARLY.csv")

"""make sure to do some preliminary checking to make sure the county names match and are the same object time to make merging easier"""

census_data_raw = pd.read_csv(CENSUS_IN_PATH, encoding="latin-1")  # CENSUS DATA

county_time_raw = pd.read_csv(ZILLOW_IN_PATH)  # ZILLOW DATA

# replace missing values with 0
county_time_raw[
    [
        "12/31/2000",
        "12/31/2001",
        "12/31/2002",
        "12/31/2003",
        "12/31/2004",
        "12/31/2005",
        "12/31/2006",
        "12/31/2007",
        "12/31/2008",
        "12/31/2009",
        "12/31/2010",
        "12/31/2011",
        "12/31/2012",
        "12/31/2013",
        "12/31/2014",
        "12/31/2015",
        "12/31/2016",
        "12/31/2017",
        "12/31/2018",
        "12/31/2019",
        "12/31/2020",
        "12/31/2021",
    ]
] = county_time_raw[
    [
        "12/31/2000",
        "12/31/2001",
        "12/31/2002",
        "12/31/2003",
        "12/31/2004",
        "12/31/2005",
        "12/31/2006",
        "12/31/2007",
        "12/31/2008",
        "12/31/2009",
        "12/31/2010",
        "12/31/2011",
        "12/31/2012",
        "12/31/2013",
        "12/31/2014",
        "12/31/2015",
        "12/31/2016",
        "12/31/2017",
        "12/31/2018",
        "12/31/2019",
        "12/31/2020",
        "12/31/2021",
    ]
].fillna(
    value=0
)

# Dictionary of full state names and abbreviations
state_to_abb = {
    # Other
    "District of Columbia": "DC",
    # States
    "Alabama": "AL",
    "Montana": "MT",
    "Alaska": "AK",
    "Nebraska": "NE",
    "Arizona": "AZ",
    "Nevada": "NV",
    "Arkansas": "AR",
    "New Hampshire": "NH",
    "California": "CA",
    "New Jersey": "NJ",
    "Colorado": "CO",
    "New Mexico": "NM",
    "Connecticut": "CT",
    "New York": "NY",
    "Delaware": "DE",
    "North Carolina": "NC",
    "Florida": "FL",
    "North Dakota": "ND",
    "Georgia": "GA",
    "Ohio": "OH",
    "Hawaii": "HI",
    "Oklahoma": "OK",
    "Idaho": "ID",
    "Oregon": "OR",
    "Illinois": "IL",
    "Pennsylvania": "PA",
    "Indiana": "IN",
    "Rhode Island": "RI",
    "Iowa": "IA",
    "South Carolina": "SC",
    "Kansas": "KS",
    "South Dakota": "SD",
    "Kentucky": "KY",
    "Tennessee": "TN",
    "Louisiana": "LA",
    "Texas": "TX",
    "Maine": "ME",
    "Utah": "UT",
    "Maryland": "MD",
    "Vermont": "VT",
    "Massachusetts": "MA",
    "Virginia": "VA",
    "Michigan": "MI",
    "Washington": "WA",
    "Minnesota": "MN",
    "West Virginia": "WV",
    "Mississippi": "MS",
    "Wisconsin": "WI",
    "Missouri": "MO",
    "Wyoming": "WY",
}


state_abb = []
for state in census_data_raw["STNAME"]:
    if state in state_to_abb.keys():
        state_abb.append(state_to_abb[state])  # append the abbriviation

census_data_raw["STABB"] = state_abb

val_list = list(state_to_abb.values())  # list of abbreviations
key_list = list(state_to_abb.keys())  # list of full name

state_names = []
for abb in county_time_raw["State"]:
    if abb in val_list:
        position = val_list.index(abb)
        state_names.append(key_list[position])

county_time_raw["STNAME"] = state_names

# create CTYNAME key col for merge
county_time_raw["CTYNAME"] = county_time_raw["RegionName"]

# select relevant cols from zillow data
zillow_raw = county_time_raw.loc[
    :,
    county_time_raw.columns.str.contains("12/31")
    | county_time_raw.columns.str.contains("CTYNAME")
    | county_time_raw.columns.str.contains("STNAME"),
]

# convert year cols into rows for zillow
zillow_melt = zillow_raw.melt(
    id_vars=["STNAME", "CTYNAME"],
    value_vars=[
        "12/31/2010",
        "12/31/2011",
        "12/31/2012",
        "12/31/2013",
        "12/31/2014",
        "12/31/2015",
        "12/31/2016",
        "12/31/2017",
        "12/31/2018",
        "12/31/2019",
    ],
    var_name="DATE",
    value_name="PRICE",
)

# make values of year columns identical for zillow
zillow_melt["YEAR"] = (zillow_melt["DATE"].str.slice(start=6)).astype("int")

# select relevant cols from census data
census_raw = census_data_raw.loc[
    :,
    census_data_raw.columns.str.contains("POPESTIMATE")
    | census_data_raw.columns.str.contains("CTYNAME")
    | census_data_raw.columns.str.contains("STNAME"),
]

# convert year cols into rows for zillow
census_melt = census_raw.melt(
    id_vars=["STNAME", "CTYNAME"], var_name="DATE", value_name="POPULATION"
)

# make values of year columns identical for census
census_melt["YEAR"] = (census_melt["DATE"].str.slice(start=11)).astype("int")

# create census index of state populations
pop_index = census_melt[census_melt["CTYNAME"] == census_melt["STNAME"]]
pop_index["STATEPOP"] = pop_index["POPULATION"]
pop_index = pop_index[["STNAME", "YEAR", "STATEPOP"]].set_index(["STNAME", "YEAR"])

# join state pop index and county pop and create weight col
census_index = census_melt.join(pop_index, on=["STNAME", "YEAR"])
census_index["POPWEIGHT"] = census_index["POPULATION"].div(census_index["STATEPOP"])

# remove state pop rows
census_index = census_index[census_index["STNAME"] != census_index["CTYNAME"]]

# merge zillow and pop
all_data = pd.merge(
    zillow_melt, census_index, how="inner", on=["STNAME", "CTYNAME", "YEAR"]
)

# round W_PRICE
all_data["W_PRICE"] = all_data["POPWEIGHT"].mul(all_data["PRICE"]).round(decimals=2)

# select relevant cols
Merged_Final = all_data[
    [
        "STNAME",
        "CTYNAME",
        "PRICE",
        "YEAR",
        "POPULATION",
        "STATEPOP",
        "POPWEIGHT",
        "W_PRICE",
    ]
]

State_Yearly = Merged_Final.round(decimals=4)

# Sort the dataframe by state name, cityname and year
Merged_Final = Merged_Final.sort_values(
    by=["STNAME", "CTYNAME", "YEAR"], ascending=[True, True, True]
)

# Use pct_change to get the percentage change of price in county level, replace nan and inf with 0
Merged_Final["Percent_change"] = (
    (Merged_Final.groupby(["STNAME", "CTYNAME"])["PRICE"].apply(pd.Series.pct_change))
    .replace([np.inf, -np.inf], np.nan)
    .fillna(0)
    .round(decimals=4)
)

# Generate total county percent change
Merged_Final["New_percent_change"] = (Merged_Final["Percent_change"] + 1).astype(float)

# Group New_percent_change by county and generate County_aggregate
County_aggregate = Merged_Final.groupby(["STNAME", "CTYNAME"]).prod(
    "New_percent_change"
)

# Get the total percentage of change
County_aggregate = (
    (County_aggregate[["New_percent_change"]] - 1).mul(100).round(decimals=2)
)

# Generate state average by summing weighted prices of counties
State_Av = (
    Merged_Final.loc[:, ["STNAME", "YEAR", "W_PRICE"]]
    .groupby(["STNAME", "YEAR"])
    .sum("W_PRICE")
    .round(decimals=2)
)

# for all counties in the same state, group by state and year
merged_final = Merged_Final.groupby(["STNAME", "YEAR"])["W_PRICE"].sum().to_frame()

# calculate percentage change from previous year
price_series = merged_final["W_PRICE"].squeeze()
price_series = price_series.pct_change() * 100

merged_final["Percentage_Change"] = price_series
merged_final["Percentage_Change"].fillna(value=0).to_frame()
merged_final["Change_From_2010"] = (
    merged_final.groupby("STNAME")["W_PRICE"]
    .apply(lambda x: x.div(x.iloc[0]).subtract(1).mul(100))
    .round(decimals=2)
)

merged_final = merged_final.reset_index()
state_aggregate = merged_final[merged_final["YEAR"] == 2019]
state_aggregate = state_aggregate[["STNAME", "Change_From_2010"]]

# Generate relevant csvs
Merged_Final.to_csv(FINAL_PATH_CTY_ANNUAL)
County_aggregate.to_csv(FINAL_PATH_CTY_TOTAL)
State_Av.to_csv(FINAL_PATH_ST_AV)
state_aggregate.to_csv(FINAL_PATH_ST_TOTAL)
State_Yearly.to_csv(FINAL_PATH_ST_ANNUAL)
