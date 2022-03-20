import csv
import os
import re
import numpy as np
import pandas as pd
import plotly.express as px
import json

IN_PATH = os.path.join("Data", "US_FIPS_Codes.csv")
IN_PATH_2 = os.path.join("Data", "STATE_YEARLY.csv")
OUTPUT_DIR = "Data"
FINAL_MERGE_PATH = os.path.join(OUTPUT_DIR, "ST_Fips_Merge.csv")


