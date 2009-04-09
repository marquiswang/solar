import urllib
import string
import models
from urllib import unquote, quote

def avg_cost(state):
    records = models.StateCost.objects.filter(state = state)
    return (records[0].avg_retail_price, records[0].avg_monthly_consumption)
