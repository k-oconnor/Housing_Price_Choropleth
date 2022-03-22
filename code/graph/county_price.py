import os
import pandas as pd
import plotly.express as px
import json

IN_PATH = os.path.join("data", "CTY_Fips_Merge.csv")
IN_PATH_JSON = os.path.join("data", "geojson-counties-fips.json")


county_fips = pd.read_csv(IN_PATH, dtype={"FIPS": str})

with open(IN_PATH_JSON) as response:
    counties = json.load(response)


def show_state(state):
    df = county_fips[county_fips["STNAME"] == state]
    state_animate = px.choropleth(
        df,
        geojson=counties,
        locations="FIPS",
        color="PRICE",
        color_continuous_scale="PuBu",
        range_color=(50000, 1000000),
        scope="usa",
        labels={"PRICE": "Housing Price"},
        animation_frame="YEAR",
        title="Change in House Values Over Time by County",
    )
    state_animate.update_geos(fitbounds="locations", visible=False)
    state_animate.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    state_animate.show()
    return


state = input("Enter a state name with uppercase first letter: ")
show_state(state)
