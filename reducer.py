#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_month = None
current_count = 0
month = None

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
            # write result to STDOUT
            print ('%s\t%s' % (current_month, current_count))
        current_count = count
        current_month = month
        

if current_month == month:
    print ('%s\t%s' % (current_month, current_count))
