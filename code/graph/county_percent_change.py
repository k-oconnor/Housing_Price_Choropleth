"""After running the 'build' scripts, this script will prompt the user to type in the name of a state.
Once a state is typed in, and the user presses ENTER, a choropleth will display of the state with all of
its counties, colored by percent change from 2010-2019."""

# Import modules
import os
import pandas as pd
import plotly.express as px
import json

# Set paths and directories
IN_PATH = os.path.join("data", "COUNTY_AGGREGATE_FIPS.csv")
IN_PATH_JSON = os.path.join("data", "geojson-counties-fips.json")

# Saves county-level dataframe into an object
county_fips = pd.read_csv(IN_PATH, dtype={"FIPS": str})

# Loads in json data that will tell plotly the corrdinates for counties
with open(IN_PATH_JSON) as response:
    counties = json.load(response)

# builds a function that will take a user input and builds a choropleth of a state broken up by counties


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
        title="Percent Change in House Values from 2010-2019 by County",
    )
    state_change.update_geos(fitbounds="locations", visible=False)
    state_change.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    state_change.show()
    return


# create exception-handling variables
states_list = county_fips['STNAME'].unique()
# print(states_list)

# prompts the user to type in a state
state = input("Enter a state name with uppercase first letter: ")

# shows choropleth and handles exceptions if state isn't valid
if state in states_list:
    show_state(state)
elif state == "end":
    print("Have a great day!")
else:
    print("You have not entered a valid State. Please rerun the program, thank you")
