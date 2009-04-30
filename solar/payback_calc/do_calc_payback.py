from solar.payback_calc.hostip import *
from decimal import Decimal

import datetime
import srlocat_wrapper
import urllib
import string
import models
from urllib import unquote, quote

def calc_infl_payback_time(installation_price, month_savings, inf_rate):
    """
        @param installation_price price of installation
        @param monthly_savings list of tuples representing (month, savings_for_month)
    
        Returns a tuple of float-valued estimated payback time and a list of
            time, payback_so_far pairs (for use in constructing a graph)

    """
    amount_paid_back = 0
    payback_years = 0

    data_entries = []
    month = 0
    acced_infl_rate = 1

    while float(amount_paid_back) < float(installation_price):
        (_, savings_for_month) = month_savings[month%len(month_savings)]
        amount_paid_back += (float(savings_for_month) * acced_infl_rate)
        if (month % 12 == 0 and month != 0): acced_infl_rate *= inf_rate
        payback_years += 1.0/12.0
        data_entries += [[payback_years, amount_paid_back]]
        month += 1

    # not entirely accurate, but good enough for our purposes. Would be better
    # to round the second part and give months. 
    payback_time = payback_years #payback_years + abs(float(amount_paid_back) -
        #float(installation_price))/yearly_amount_saved

    #data_entries[-1] = [payback_time, installation_price]
    
    return payback_time, data_entries


def calc_monthly_savings(cost_per_month, lat, lng, today, \
                        peak_power_output, tiers = 0, buyback_price = 0, debug = 0):
    """
        @param cost_per_month: List of tuples of (cost, usage) for months 
            (Jan first) where cost is in c/wh
        @param tiers: List of tuples of (max_usage, cost_per_watts) representing
            pricing tiers (cost_per_watts is in c/wh)
        @param buyback_price: Should be in c/wh
    """

    month = 1
    monthly_savings = [] # $ saved by subtraction of generated 
                            # electricity from total usage
    for (cost, usage) in cost_per_month:
        if (month == 12):
            days_in_month = 31
        else:
            days_in_month = (datetime.date(today.year-1, month + 1, 1) \
                        - datetime.date(today.year-1, month, 1)).days

        amount_generated_per_day = \
            avg_pow_gen_day(lat, lng, today.year-1, month, peak_power_output)

        amount_generated = amount_generated_per_day * days_in_month

        if (amount_generated > usage):
            if buyback_price:
                monthly_savings += \
                    [(month, float(cost)+(amount_generated*buyback_price))] 
            else:   
                monthly_savings += [(month, cost)]
        # If we have tiered pricing, we should calculate starting with the
        # lowest tier and working up.
        elif tiers:
            cost_this_month = 0
            accounted_for = 0
            for (cost_per_watt, max_usage) in tiers:
                if (max_usage > usage or max_usage == 0):
                    cost_this_month += (float(cost_per_watt)/100.0) * \
                                       (float(usage) - float(accounted_for))
                    break
                else:
                    cost_this_month += float(cost_per_watt) * \
                                       (float(max_usage) - float(accounted_for))
                    accounted_for = max_usage
            if (float(cost) < float(cost_this_month)): cost_this_month = cost
            assert(float(cost)>float(cost_this_month))
            monthly_savings += [(month, float(cost)-float(cost_this_month))]
        # Otherwise, just use the ratio of cost to usage from prior
        # information to get a rate.
        else:
            monthly_savings += [(month, amount_generated * \
                (float(cost)/float(usage)))]
        month+=1
    return monthly_savings

def avg_cost(state):
    records = models.StateCost.objects.filter(state = state)
    return (records[0].avg_monthly_bill, records[0].avg_monthly_consumption)

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
        (lookup_insolation(lat, lng, year, month)/testing_condition)*24)
