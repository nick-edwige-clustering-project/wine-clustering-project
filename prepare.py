import pandas as pd
import numpy as np


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

import explore as ex


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
    wine = pd.concat([red,white])
    wine = wine.reset_index().drop(columns='index')
    wine.columns = wine.columns.str.replace(' ','_')
    
    return wine


def train_val_test(df, strat='None', seed=100, stratify=False):  # Splits dataframe into train, val, test
    """ This function will split my data into train, validate and test. It has the option to stratify."""
    if stratify:  # Will split with stratify if stratify is True
        train, val_test = train_test_split(df, train_size=0.7, random_state=seed, stratify=df[strat])
        val, test = train_test_split(val_test, train_size=0.5, random_state=seed, stratify=val_test[strat])
        return train, val, test
    if not stratify:  # Will split without stratify if stratify is False
        train, val_test = train_test_split(df, train_size=0.7, random_state=seed)
        val, test = train_test_split(val_test, train_size=0.5, random_state=seed)
        return train, val, test
    

def scale(dataframe, train=None, val=None, test=None, method='mms', scaled_cols=None, split=True):
    """This function will take in a dataframe or the train, val, test dataframes and scale the data according to
    whatever method is chosen."""
    df = dataframe.copy()
    if split is not True:
        if method == 'mms':  # MinMax is chosen
            mms = MinMaxScaler()
            mms.fit(df[scaled_cols])
            df[scaled_cols] = mms.transform(df[scaled_cols])
            return df  # returns df
        if method == 'ss':  # Standard is chosen
            ss = StandardScaler()
            ss.fit(df[scaled_cols])
            df[scaled_cols] = ss.transform(df[scaled_cols])
            return df  # returns df
        if method == 'rs':  # Robust is chosen
            rs = RobustScaler()
            rs.fit(df[scaled_cols])
            df[scaled_cols] = rs.transform(df[scaled_cols])
            return df  # returns df

    if split is True:
        if train is None or val is None or test is None:
            train, val, test = train_val_test(df)
        if scaled_cols is None:
            scaled_cols = ['bedrooms', 'bathrooms', 'sq_ft', 'year', 'lot_sq_ft']
        if method == 'mms':  # MinMax is chosen
            mms = MinMaxScaler()
            mms.fit(train[scaled_cols])
            train[scaled_cols] = mms.transform(train[scaled_cols])
            val[scaled_cols] = mms.transform(val[scaled_cols])
            test[scaled_cols] = mms.transform(test[scaled_cols])
            return train, val, test
        if method == 'ss':  # Standard is chosen
            ss = StandardScaler()
            ss.fit(train[scaled_cols])
            train[scaled_cols] = ss.transform(train[scaled_cols])
            val[scaled_cols] = ss.transform(val[scaled_cols])
            test[scaled_cols] = ss.transform(test[scaled_cols])
            return train, val, test
        if method == 'rs':  # Robust is chosen
            rs = RobustScaler()
            rs.fit(train[scaled_cols])
            train[scaled_cols] = rs.transform(train[scaled_cols])
            val[scaled_cols] = rs.transform(val[scaled_cols])
            test[scaled_cols] = rs.transform(test[scaled_cols])
            return train, val, test  # returns train test and val

        
def dummies(train, val, test, drop_first=None, normal_list=None):
    """This function will one hot encode a dataframe. It accepts one or more dataframes, and two lists of columns."""
    if drop_first is not None:
        train = pd.get_dummies(train, columns=drop_first, drop_first=True)  # Drops first value from columns
        val = pd.get_dummies(val, columns=drop_first, drop_first=True)
        test = pd.get_dummies(test, columns=drop_first, drop_first=True)

    if normal_list is not None:
        train = pd.get_dummies(train, columns=normal_list)  # Does not drop first from this list of columns
        val = pd.get_dummies(val, columns=normal_list)
        test = pd.get_dummies(test, columns=normal_list)

    return train, val, test  # Returns encoded dataframes


def split_xy(df, target=''):
    """This function will split x and y according to the target variable."""
    x_df = df.drop(columns=target)
    y_df = df[target]
    return x_df, y_df  # Returns dataframe


def readjust_range(wine):
    '''
    trims 5% of total data to remove outliers.
    '''
    wine = wine[(wine.fixed_acidity < 12) & (wine.fixed_acidity > 4.5)]
    wine = wine[wine.volatile_acidity < 0.8]
    wine = wine[wine.citric_acid < 0.8]
    wine = wine[wine.residual_sugar < 22]
    wine = wine[wine.chlorides < .12]
    wine = wine[wine.free_sulfur_dioxide < 80]
    wine = wine[wine.total_sulfur_dioxide < 275]
    wine = wine[wine.density < 1.01]
    wine = wine[wine.pH < 3.8]
    wine = wine[wine.sulphates < 1.00]
    # wine = wine[wine.alcohol < 1000]
    return wine


def pour():
    '''
    pipeline funtion. runs entire pipeline returns cleaned df
    '''
    wine = all_data()
    wine = readjust_range(wine)
    return wine

def drink_up(wine):
    '''
    splits df for train, val, test
    and further into x and y splits
    test will be split by itlsef later
    '''
    train, val, test = train_val_test(wine, strat='quality', seed=100)
    train, val, test = scale(wine, train=train, val=val, test=test, scaled_cols=(wine.select_dtypes(float).columns))
    train, val, test = dummies(train, val, test, drop_first=['wine_type'])
    x_train, y_train = split_xy(train, 'quality')
    x_val, y_val = split_xy(val, 'quality')
    return  x_train, y_train, x_val, y_val, test