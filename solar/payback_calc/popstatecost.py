#/bin/python
import models

def importIntoStateCost(filename):
    lines = open(filename).readlines()
    for i in lines:
        fields = i.split()
        new = models.StateCost(state = fields[0], num_consumers = int(fields[1]), \
                avg_monthly_consumption = int(fields[2]), \
                avg_retail_price = float(fields[3]), \
                avg_monthly_bill = float(fields[4]))

        new.save()
