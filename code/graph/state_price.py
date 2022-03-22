"""This script will generate a choropleth of the United States where each state is colored by
it weighted average housing price paired with a slider that goes between 2010-2019."""

# import modules
import os
import pandas as pd
import plotly.express as px
import json

# Set directories and paths
IN_PATH = os.path.join("data", "ST_yoy_avg_fips_Merge.csv")
IN_PATH_JSON = os.path.join("data", "us-states.json")

# Saves appropriate state-level dataframe into an object
state_fips_yoy = pd.read_csv(IN_PATH, dtype={"FIPS": str})

# Loads in json data that will tell plotly the corrdinates for states
with open(IN_PATH_JSON) as response:
    states = json.load(response)

# Generates and displays the appropriate choropleth
fig_animate = px.choropleth(
    state_fips_yoy,
    geojson=states,
    locations="FIPS",
    color="W_PRICE",
    color_continuous_scale="PuBu",
    range_color=(0, 600000),
    scope="usa",
    labels={"W_PRICE": "Weighted Price"},
    animation_frame="YEAR",
    title="Year-Over-Year Change in Weighted Mean Price per State",
)
fig_animate.show()
