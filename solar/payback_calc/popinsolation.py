#/bin/python
import models

def import_into_insolation(filename):
    lines = open(filename).readlines()
    for i in lines[14:]:
        fields = i.split()

        for month in range(1,13):
            new = models.Insolation(lat = fields[0],\
                                    lon = fields[1],\
                                    daily_insolation = fields[1+month],\
                                    month = month)
            new.save()
