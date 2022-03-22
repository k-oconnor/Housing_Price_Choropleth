"""This script will generate a choropleth of the United States where each state is colored by
it percent change in housing prices over the period of 2010-2019."""

# import modules
import os
import pandas as pd
import plotly.express as px
import json

# sets paths and directories
IN_PATH = os.path.join("data", "ST_Agg_Fips_Merge.csv")
IN_PATH_JSON = os.path.join("data", "us-states.json")

# takes the appropriate dataframe and saves it into an object.
state_fips = pd.read_csv(IN_PATH, dtype={"FIPS": str})

# Loads in json data that will tell plotly the corrdinates for states
with open(IN_PATH_JSON) as response:
    states = json.load(response)

# creates and displays the appropriate choropleth
fig = px.choropleth(
    state_fips,
    geojson=states,
    locations="FIPS",
    color="Change_From_2010",
    color_continuous_scale="PuBu",
    range_color=(0, 125),
    scope="usa",
    labels={"Change_From_2010": "Percent Change in Housing Price"},
    title="Percent Change in House Values from 2010-2019 by State",
)
fig.show()
