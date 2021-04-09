import numpy as np 
import pandas as pd 

def acquire_wine_data():
    df =  pd.read_csv('wine_quality.csv', sep=' ', header=None)
    
    return df

