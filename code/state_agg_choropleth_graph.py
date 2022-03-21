import os
import pandas as pd
import plotly.express as px
import json

IN_PATH = os.path.join("Data", "ST_Agg_Fips_Merge.csv")
IN_PATH_JSON = os.path.join("Data", "us-states.json")


state_fips = pd.read_csv(IN_PATH,dtype={'FIPS':str})
# print(state_fips)

with open (IN_PATH_JSON) as response:
    states = json.load(response)


fig= px.choropleth(state_fips, geojson=states, locations = 'FIPS', color = 'Change_From_2010',
                       color_continuous_scale= "PuBu",range_color=(0,125),scope = "usa", labels={'Change_From_2010':'Percent Change from 2010'}, title = "Percent Change in House Values over Time")
fig.show()