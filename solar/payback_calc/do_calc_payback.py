from solar.payback_calc.srlocat_wrapper import avg_sunlight
from solar.payback_calc.hostip import *
from solar.payback_calc.avg_cost import avg_cost

def calc_infl_payback_time(installation_price, yearly_amount_saved, inf_rate):
    """
    calc_infl_payback_time: calculate the payback time taking inflation into account
    
    Returns float-valued estimated payback time
    """
    amount_paid_back = 0
    payback_years = 0

    while float(amount_paid_back) < float(installation_price):
        amount_paid_back += yearly_amount_saved
        yearly_amount_saved_adj *= inf_rate
        payback_years += 1

    # not entirely accurate, but good enough for our purposes. Would be better to round the second part and give months. 
    payback_time = payback_years + (float(amount_paid_back) - float(installation_price))/yearly_amount_saved
    
    return payback_time
    
