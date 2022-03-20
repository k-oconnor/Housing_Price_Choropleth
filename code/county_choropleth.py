import csv
import os
import re
import numpy as np
import pandas as pd
import plotly.express as px
import json

IN_PATH = os.path.join("Data", "CTY_Fips_Merge.csv")
IN_PATH_JSON = os.path.join("Data", "geojson-counties-fips.json")


county_fips = pd.read_csv(IN_PATH, dtype={"FIPS": str})

with open(IN_PATH_JSON) as response:
    counties = json.load(response)

# 2011
twenty_eleven = county_fips[county_fips["YEAR"] == 2011]
print(twenty_eleven)

figure = px.choropleth(
    twenty_eleven,
    geojson=counties,
    locations="FIPS",
    color="New_percent_change",
    color_continuous_scale="Bluered_r",
    range_color=(0.9, 1.2),
    scope="usa",
    labels={"New_percent_change": "Percent Change in Housing Price"},
)
figure.show()

# 2012
twenty_twelve = county_fips[county_fips["YEAR"] == 2012]

figure1 = px.choropleth(
    twenty_twelve,
    geojson=counties,
    locations="FIPS",
    color="New_percent_change",
    color_continuous_scale="Bluered_r",
    range_color=(0.9, 1.2),
    scope="usa",
    labels={"New_percent_change": "Percent Change in Housing Price"},
)
figure.show()

# 2013
twenty_thirteen = county_fips[county_fips["YEAR"] == 2013]

figure2 = px.choropleth(
    twenty_thirteen,
    geojson=counties,
    locations="FIPS",
    color="New_percent_change",
    color_continuous_scale="Bluered_r",
    range_color=(0.9, 1.2),
    scope="usa",
    labels={"New_percent_change": "Percent Change in Housing Price"},
)
figure2.show()

# 2014
twenty_fourteen = county_fips[county_fips["YEAR"] == 2014]

figure3 = px.choropleth(
    twenty_fourteen,
    geojson=counties,
    locations="FIPS",
    color="New_percent_change",
    color_continuous_scale="Bluered_r",
    range_color=(0.9, 1.2),
    scope="usa",
    labels={"New_percent_change": "Percent Change in Housing Price"},
)
figure3.show()

# 2015
twenty_fifteen = county_fips[county_fips["YEAR"] == 2015]

figure4 = px.choropleth(
    twenty_fifteen,
    geojson=counties,
    locations="FIPS",
    color="New_percent_change",
    color_continuous_scale="Bluered_r",
    range_color=(0.9, 1.2),
    scope="usa",
    labels={"New_percent_change": "Percent Change in Housing Price"},
)
figure4.show()

# 2016
twenty_sixteen = county_fips[county_fips["YEAR"] == 2016]

figure5 = px.choropleth(
    twenty_sixteen,
    geojson=counties,
    locations="FIPS",
    color="New_percent_change",
    color_continuous_scale="Bluered_r",
    range_color=(0.9, 1.2),
    scope="usa",
    labels={"New_percent_change": "Percent Change in Housing Price"},
)
figure5.show()

# 2017
twenty_seventeen = county_fips[county_fips["YEAR"] == 2017]

figure6 = px.choropleth(
    twenty_seventeen,
    geojson=counties,
    locations="FIPS",
    color="New_percent_change",
    color_continuous_scale="Bluered_r",
    range_color=(0.9, 1.2),
    scope="usa",
    labels={"New_percent_change": "Percent Change in Housing Price"},
)
figure6.show()

# 2018
twenty_eighteen = county_fips[county_fips["YEAR"] == 2018]

figure7 = px.choropleth(
    twenty_eighteen,
    geojson=counties,
    locations="FIPS",
    color="New_percent_change",
    color_continuous_scale="Bluered_r",
    range_color=(0.9, 1.2),
    scope="usa",
    labels={"New_percent_change": "Percent Change in Housing Price"},
)
figure7.show()

# 2019
twenty_nineteen = county_fips[county_fips["YEAR"] == 2018]

figure8 = px.choropleth(
    twenty_nineteen,
    geojson=counties,
    locations="FIPS",
    color="New_percent_change",
    color_continuous_scale="Bluered_r",
    range_color=(0.9, 1.2),
    scope="usa",
    labels={"New_percent_change": "Percent Change in Housing Price"},
)
figure8.show()

fig_animate = px.choropleth(
    county_fips,
    geojson=counties,
    locations="FIPS",
    color="New_percent_change",
    color_continuous_scale="Bluered_r",
    range_color=(0.9, 1.2),
    scope="usa",
    labels={"New_percent_change": "Percent Change in Housing Price"},
    animation_frame="YEAR",
    title="Percent Change in House Values over Time",
)
fig_animate.show()
