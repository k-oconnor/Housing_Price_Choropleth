import os
import pandas as pd
import plotly.express as px
import json

IN_PATH = os.path.join("Data", "ST_yoy_avg_fips_Merge.csv")
IN_PATH_JSON = os.path.join("Data", "us-states.json")


state_fips_yoy = pd.read_csv(IN_PATH, dtype={"FIPS": str})


with open(IN_PATH_JSON) as response:
    states = json.load(response)


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
