import csv
import os
import re
import numpy as np
import pandas as pd
import plotly.express as px
import json

IN_PATH = os.path.join("Data", "COUNTY_AGGREGATE_FIPS.csv")
IN_PATH_JSON = os.path.join("Data", "geojson-counties-fips.json")


county_fips = pd.read_csv(IN_PATH, dtype={"FIPS": str})

with open(IN_PATH_JSON) as response:
    counties = json.load(response)


def show_state(state):
    df = county_fips[county_fips["STNAME"] == state]
    state_change = px.choropleth(
        df,
        geojson=counties,
        locations="FIPS",
        color="New_percent_change",
        color_continuous_scale="PuBu",
        range_color=(0, 100),
        scope="usa",
        labels={"New_percent_change": "Percent Change in Housing Price"},
        title="Percent Change in House Values over Time",
    )
    state_change.update_geos(fitbounds="locations", visible=False)
    state_change.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    state_change.show()
    return


state = input("Enter a state name with uppercase first letter: ")
show_state(state)
