

#--------------------------------------------------------------------------
# Import libraries
#--------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime 
import sklearn
from Modules import clean_data

#--------------------------------------------------------------------------
# Data Clean
#--------------------------------------------------------------------------

try: #Start class for data cleaning
    dc = clean_data.CleanData('./Turbine_Data.csv')
    print("data cleaning class started correctly")
except Exception as e:
    print(f"the robot failed to start the data cleaning class: {e}")
    result = str(e)
    exit(1)

try:
    df = dc.ReadData(',')
    print(df)
    print("the robot succeeded to read the file")
except Exception as e:
    print(f"the robot failed to read the input data: {e}")
    result = str(e)
    exit(1)
    