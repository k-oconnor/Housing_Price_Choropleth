import csv
import os
import re
import numpy as np
import pandas as pd
import plotly.express as px
import json

IN_PATH = os.path.join("data", "ST_Fips_Merge.csv")
IN_PATH_JSON = os.path.join("data", "gz_2010_us_040_00_500k (1).json")

state_fips = pd.read_csv(IN_PATH,dtype={'FIPS':str})