## Data Fetcher for green tripdata 
## Load data per year and month range

import os
import sys
from pathlib import Path
import numpy as np

def download_data(month_start,month_end,year):
    dataset = "green_tripdata"
    # Define month range
    myList = np.linspace(int(month_start),int(month_end),int(month_end)) # From month a->b

    Path(f'./data/{year}/').mkdir(parents=True,exist_ok=True)
    for a in myList:
        print(f"-_-_-_-_-_- Fetching Data for {year}/{int(a)} ")
        
        os.system(f"wget -O ./data/{year}/{dataset}_{year}-0{a.astype(int)}.parquet \
            https://s3.amazonaws.com/nyc-tlc/trip+data/{dataset}_{year}-0{a.astype(int)}.parquet")


if __name__ == '__main__':
    year = sys.argv[1]
    month_start = sys.argv[2]
    month_end = sys.argv[3]
    download_data(month_start,month_end, year)
        