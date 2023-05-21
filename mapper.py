#!/usr/bin/env python
"""mapper.py"""

import sys
import pandas as pd
import numpy as np


#read in dataframe
df = pd.read_csv(sys.stdin)

#Select only the bookings that weren't cancelled
if np.issubdtype(df['booking_status'].dtype, np.number):
    df = df[df.booking_status == 0]
else:
    df = df[df.booking_status == "Not_Canceled"]
    
#calculate a price for the room
df["total_price"] = (df.stays_in_weekend_nights + df.stays_in_week_nights) * df.avg_price_per_room

#Convert numbers to months
months = {1: 'January',
 2: 'February',
 3: 'March',
 4: 'April',
 5: 'May',
 6: 'June',
 7: 'July',
 8: 'August',
 9: 'September',
 10: 'October',
 11: 'November',
 12: 'December'}
if np.issubdtype(df['arrival_month'].dtype, np.number):
    df["arrival_month"] = df["arrival_month"].apply(lambda x: months[x])
    
for month,price in zip(df.arrival_month,df.total_price):
    print ('%s\t%s' % (month, price))
