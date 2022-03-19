#import modules
import csv
import os
import numpy as np
import pandas as pd

#Define import and export pathways 
IN_PATH = os.path.join("artifacts", 'zillow_census_clean.csv')
OUTPUT_DIR = "data"
FINAL_PATH_TOTAL = os.path.join(OUTPUT_DIR, 'STATE_AGGREGATE.csv')
FINAL_PATH_ANNUAL = os.path.join(OUTPUT_DIR, 'STATE_YEARLY.csv')

#Read previously generated csv file
Merged_Final = pd.read_csv(IN_PATH)

#Sort the dataframe by state name, cityname and year
Merged_Final= Merged_Final.sort_values(by = ['STNAME', 'CTYNAME', 'YEAR'], ascending=[True,True,True])

#Use pct_change to get the percentage change of price in county level, replace nan and inf with 0
Merged_Final['Percent_change'] = (Merged_Final.groupby(['STNAME','CTYNAME'])['PRICE']
.apply(pd.Series.pct_change)).replace([np.inf, -np.inf], np.nan).fillna(0)

#Generate total county percent change
Merged_Final['New_percent_change'] = (Merged_Final['Percent_change'] + 1).astype(float)

#Multiple Percent_change by 100
Merged_Final['Percent_change'] = Merged_Final['Percent_change']

# Group New_percent_change by county and generate County_aggregate
County_aggregate = Merged_Final.groupby(['STNAME', 'CTYNAME']).prod('New_percent_change')

# Get the total percentage of change 
County_aggregate = (County_aggregate[['New_percent_change']] -1).mul(100)

#print the annual percentage change per county from 2010 to 2019
print(Merged_Final)

#print the aggregate percentage change per county between 2010 and 2019
print(County_aggregate)

#Generate two csv
#Merged_Final.to_csv(FINAL_PATH_ANNUAL)
# County_aggregate.to_csv(FINAL_PATH_TOTAL)