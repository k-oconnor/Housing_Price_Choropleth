"""After running the 'build' scripts, this script will prompt the user to type in the name of a state.
Once a state is typed in, and the user presses ENTER, an interactive choropleth that will display of the state with all of
its counties, colored the weighted average price paired with a slider that goes from 2010-2019."""

# Import modules
import os
import pandas as pd
import plotly.express as px
import json

# Set paths and directories
IN_PATH = os.path.join("data", "CTY_Fips_Merge.csv")
IN_PATH_JSON = os.path.join("data", "geojson-counties-fips.json")

# Saves county-level dataframe into an object
county_fips = pd.read_csv(IN_PATH, dtype={"FIPS": str})

# Loads in json data that will tell plotly the corrdinates for counties
with open(IN_PATH_JSON) as response:
    counties = json.load(response)

# builds a function that will take a user input and builds a choropleth of a state broken up by counties


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


# prompts the user to type in a state
state = input("Enter a state name with uppercase first letter: ")
state = state.title()

# displays choropleth and handles exceptions if state isnt valid
states_list = county_fips['STNAME'].unique()

if state in states_list:
    show_state(state)
elif state == "end":
    print("Have a great day!")
else:
    print("You have not entered a valid State. Please rerun the program, thank you.")
