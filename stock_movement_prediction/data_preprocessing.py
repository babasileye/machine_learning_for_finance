import numpy as np
import pandas as pd

def compute_price_movement(current_mean,current_std,next_mean):
    '''
    Compute price movement.
    If |next_mean-current_mean|<=current_std:no movement (0)
    If next_mean<current_mean-current_std:movement down (-1)
    If next_mean>current_mean+next_std:movement up (1)
    '''
    if next_mean<current_mean-current_std:
        return -1
    elif next_mean>current_mean+current_std:
        return 1
    else:
        return 0

def price_preprocessing(price_df,time_period):
    '''
    Preprocess stock daily prices into normalized prices sequences (price minus mean price divided by
    standard deviation) over specified periods.
    Normalized prices will be used independant variables, while price movements are used as predicted variable.
    Inputs:
    price_df: daily prices (every column represents an asset's  price time series)
    time_period: period's size
    Outputs:
    preprocessed_df: preprocessed data frame with corresponding columns:
    "ticker_price": asset-price key
    "normalized_price_sequence": mean-variance normalized prices of a period
    "price_movement":
        1:next perdiod's mean price is below a standard deviation of the currents periods mean
        0:next period's mean price is within a standard deviation of the current's period's mean
        1:next perdiod's mean price is above a standard deviation of the currents periods mean
    '''
    data=[]
    for key in price_df.keys():
        current_mean=price_df[key][0:time_period].mean()
        current_std=price_df[key][0:time_period].std()
        for t in range(time_period,price_df.shape[0]-time_period,time_period):
            normalized_prices=[(p-current_mean)/current_std for p in price_df[key][t-time_period:t].tolist()]
            next_mean=price_df[key][t:t+time_period].mean()
            next_std=price_df[key][t:t+time_period].std()
            price_movement=compute_price_movement(current_mean,current_std,next_mean)
            buffer={
                'ticker_price':key,
                'normalized_price_sequence':normalized_prices,
                'sequence_mean':current_mean,
                'sequence_std':current_std,
                'next_sequence_mean':next_mean,
                'price_movement':price_movement}
            data.append(buffer)
            current_mean=next_mean
            current_std=next_std
    preprocessed_df=pd.DataFrame.from_dict(data)
    return preprocessed_df
