import csv
import os
import re
import numpy as np
import pandas as pd
import plotly.express as px
import json
import plotly.graph_objects as go

IN_PATH = os.path.join("data", "ST_Fips_Merge.csv")
IN_PATH_JSON = os.path.join("data", "us-states.json")

df = pd.read_csv(IN_PATH)
df['text'] = 'State:' + df['STNAME']

# fig = go.Figure(data=go.choropleth(
#     locations = df['STNAME'],
#     z = df['YEAR'].astype(float),
#     locationmode = 'USA-states',
#     colorscale = 'Blues',
#     colorbar_title = 'Percent Change in Housing Prices from 2010',
#     text = df['text'],)
# )

# fig.show()




state_fips = pd.read_csv(IN_PATH,dtype={'FIPS':str})

with open (IN_PATH_JSON) as response:
    states = json.load(response)

twenty_eleven = state_fips[state_fips['YEAR']== 2011]

# print(twenty_eleven)

figure1 = px.choropleth(twenty_eleven, geojson=states, locations = 'STNAME', color = 'Change_From_2010',
                       color_continuous_scale= "Bluered_r",scope = "usa", labels={'Change_From_2010':'Percent Change from 2010 in Housing Price'})
figure1.show()
print(twenty_eleven)