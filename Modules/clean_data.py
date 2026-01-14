#--------------------------------------------------------------------------
# Import libraries
#--------------------------------------------------------------------------

import pandas as pd

#--------------------------------------------------------------------------
# Create Class
#--------------------------------------------------------------------------

class CleanData:

    def __init__(self, path:str):
        self.path = path

    def ReadData(self, separator:str):
        df = pd.read_csv(filepath_or_buffer=self.path,
                         sep=separator)
        
        print(df.describe())
        print("------------------------" \
        "-----------------------")
        print(df.info())
        print("------------------------")
        
        return df
    
    def DataInfo(self, df):
        print("work in progress")