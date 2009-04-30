# Script for importing the insolation data into an appropriate database.
import urllib
import string
import models
from urllib import unquote, quote
import srlocat_wrapper

def lookup_insolation(lat, lon, year, month):
    """
        @lat: latitude
        @long: longitude
        @year: year (only used if DB does not have data)
        @month: month

        outputs daily average sunlight for the given latitude, longitude, 
            month (kwh/m2/day)
    """
    records = models.Insolation.objects.filter(lat=int(lat), \
        lon=int(lon), month=month)
    if (records == []):
        # Fall back to the fortran script, just average the days
        average_per_days = [i for (i,j) in \
            srlocat_wrapper.srlocat(lat, lon, year, month)]
        # Grab average over days and divide by 1000
        return sum(average_per_days)/float(len(average_per_days))/1000
    else:
        # Use the database information
        return records[0].daily_insolation 

def avg_pow_gen_day(lat, lng, year, month, panel_max, testing_condition = 1000):
    return (panel_max*\
        (lookup_insolation(lat, lng, year, month)/testing_conditions)*24)
