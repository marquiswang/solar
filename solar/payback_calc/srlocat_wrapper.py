from subprocess import Popen,PIPE
import os
import sys

def parse_line(srline):
    splitline = srline.split()
    return (float(splitline[-2]), float(splitline[-1]))

def srlocat(lat, long, year, month, day = 0):
    """
        srlocat: wrapper for the fortran insolation calculator
        @lat: latitude
        @long: longitude
        @year: year
        @month: month

        outputs a list of tuples of the form 
            (daily average sunlight (W/m^2), sunlight weighted average of zenith angle)
    """
    if day != 0:
        month_data = srlocat(lat, long, year, month)
        if day <= len(month_data):
            return month_data[day-1]
        else:
            return (0, 0)
    else:
        command = ["srlocat"]
        args = [str(i) for i in [lat, long, year, month]]
        srlocat_process = Popen(command+args, stdout=PIPE)
        srlocat_output = \
            [i.rstrip('\n').lstrip(' ') for i in srlocat_process.stdout.readlines()]
        srlocat_output = filter(\
            lambda x: x!="" and (x[0] in "0123456789"), srlocat_output)
        return [parse_line(i) for i in srlocat_output]

