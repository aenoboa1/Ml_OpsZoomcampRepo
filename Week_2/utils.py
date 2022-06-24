
## Load data per year

import os
import sys
from pathlib import Path
import numpy as np

    
#def __init__(self):
#    self.month = sys.argv[0]
#    self.year = sys.argv[1]

def download_data(month,year):
    dataset = "green_tripdata"
    # Define month range
    myList = np.linspace(1,3,3) # From Jan to Feb

    Path(f'./data/{year}/').mkdir(parents=True,exist_ok=True)
    for a in myList:
        print(f"-_-_-_-_-_- Fetching Data for {year}/{month} ")
        
        os.system(f"wget -O ./data/2021/{dataset}_{year}-0{a.astype(int)}.parquet \
            https://s3.amazonaws.com/nyc-tlc/trip+data/{dataset}_{year}-0{a.astype(int)}.parquet")
        
    
if __name__ == '__main__':
    month = sys.argv[1]
    year = sys.argv[2]
    download_data(month, year)
        