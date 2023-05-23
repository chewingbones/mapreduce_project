#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_month = None
current_count = 0
month = None
sorted_list = []

# input comes from STDIN
for line in sys.stdin:
    
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    month, count = line.split('\t', 1)
    
    # convert count (currently a string) to float
    count = float(count)
        
    
    
    if current_month == month:
        current_count += count
    else:
        if current_month:
            # append to list to be sorted later
            
            sorted_list.append((current_month, current_count))
        current_count = count
        current_month = month
        
#append final result 
if current_month == month:
    
    sorted_list.append((current_month, current_count))
#sorts by total_price
sorted_list = sorted(sorted_list, key=lambda x: x[1], reverse = True)
#outputs all of the months; can easily be ammended to output largest month
#we also wouldn't have to sort the list if we just want the largest value
for item in sorted_list:
    print ('%s\t%s' % (item[0], item[1]))
