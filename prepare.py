import pandas as pd
import numpy as np


# Data is pulled from https://data.world/food/wine-quality
def all_data():
    '''
    combines all data with a concat
    adds catagory called wine type and labels apporriatly
    RETURNS df
    '''
    red = pd.read_csv('winequality-red.csv')
    white = pd.read_csv('winequality-white.csv')
    red['wine_type'] = 'red'
    white['wine_type'] = 'white'
    wines = pd.concat([red,white])
    
    return wines