import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def get_wine_data():
    '''
    Grab our data from path and read as dataframe
    '''
    
    df = pd.read_csv('wine_quality.csv')
    
    return df