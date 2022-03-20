
import csv
import os
import numpy as np
import pandas as pd

IN_PATH = os.path.join("artifacts", 'zillow_census_clean.csv')
OUTPUT_DIR = "data"
FINAL_PATH_TOTAL = os.path.join(OUTPUT_DIR, 'STATE_AGGREGATE.csv')
FINAL_PATH_ANNUAL = os.path.join(OUTPUT_DIR, 'STATE_YEARLY.csv')

Merged_Final = pd.read_csv(IN_PATH)

#for all counties in the same state, group by state and year
merged_final = Merged_Final.groupby(['STNAME', 'YEAR'])['W_PRICE'].sum().to_frame()

#calculate percentage change from previous year
price_series = merged_final['W_PRICE'].squeeze()
price_series = price_series.pct_change() * 100

merged_final['Percentage_Change'] = price_series
merged_final['Percentage_Change'].fillna(value = 0).to_frame()
merged_final['Change_From_2010'] = merged_final.groupby('STNAME')['W_PRICE'].apply(lambda x: x.div(x.iloc[0]).subtract(1).mul(100))
print(merged_final)
merged_final = merged_final.reset_index()
state_aggregate = merged_final[merged_final['YEAR']== 2019]
state_aggregate = state_aggregate[['STNAME','Change_From_2010']]
print(state_aggregate)

#Generate two csv
merged_final.to_csv(FINAL_PATH_ANNUAL) #'percentage_change' column is the relevant year-on-year change
state_aggregate.to_csv(FINAL_PATH_TOTAL)