from solar.payback_calc.srlocat_wrapper import avg_sunlight
from solar.payback_calc.hostip import *
from solar.payback_calc.avg_cost import avg_cost

def calc_infl_payback_time(installation_price, yearly_amount_saved, inf_rate):
    """
        @param calc_infl_payback_time calculate the payback time taking
            inflation into account
    
        Returns a tuple of float-valued estimated payback time and a list of
            time, payback_so_far pairs (for use in constructing a graph)

    """
    amount_paid_back = 0
    payback_years = 0

    data_entries = []

    while float(amount_paid_back) < float(installation_price):
        amount_paid_back += yearly_amount_saved
        yearly_amount_saved *= inf_rate
        payback_years += 1
        data_entries += [[payback_years, amount_paid_back]]

    # not entirely accurate, but good enough for our purposes. Would be better
    # to round the second part and give months. 
    payback_time = payback_years + abs(float(amount_paid_back) -
        float(installation_price))/yearly_amount_saved

    data_entries[-1] = [payback_time, installation_price]
    
    return payback_time, data_entries


def calc_yearly_savings(cost_per_month, lat, lng, today, \
                        peak_power_output, tiers = 0):
    """
        @param cost_per_month: List of tuples of (cost, usage) for months 
            (Jan first)
        @param tiers: List of tuples of (max_usage, cost_per_watts) representin
            pricing tiers.
    """

    month = 1
    yearly_amount_saved = 0 # $ saved by subtraction of generated 
                            # electricity from total usage
    for (cost, usage) in cost_per_month:
        amount_generated = \
            avg_sunlight(lat, lng, today.year-1, month, peak_power_output)/1000

        # If we have tiered pricing, we should calculate starting with the
        # lowest tier and working up.
        if tiers:
            cost_this_month = 0
            accounted_for = 0
            for (max_usage, cost_per_watt) in tiers:
                if (max_usage > usage or max_usage == 0):
                    cost_this_month += cost_per_watt * \
                                       (usage - accounted_for)
                    break
                else:
                    cost_this_month += cost_per_watt * \
                                       (max_usage - accounted_for)
                    accounted_for = max_usage
            yearly_amount_saved += cost - cost_this_month
        # Otherwise, just use the ratio of cost to usage from prior
        # information to get a rate.
        else:
            yearly_amount_saved += amount_generated * \
                (float(cost)/float(usage))
        month+=1
    return yearly_amount_saved

