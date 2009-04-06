from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from formdef import SolarForm
from srlocat_wrapper import srlocat

import math

def index(request):
    """
        This is a stub.  When this function is called, the main page of the
        payback calculator should load.  templates/index.html should have
        the form.
    """
    form = SolarForm() # An unbound form
    return render_to_response('index.html', {'form': form})



def calc_payback(request):
    """
        This is a stub for rendering the response to the form in index.html.
        calc_payback should handle handing the information from the response
        to the relevant logic and should assemble the response into a response
        using the response.html template at templates/response.html.
    """
    if request.method != 'POST': # If the form has been submitted...
        return render_to_response('error.html', {})

    form = SolarForm(request.POST) # A form bound to the POST data
    
    monthly_energy_output = []
    # Doesn't work, need to figure out how to get data from form. 
    for m in range(0, 12):
        month = m+1
        insolation = srlocat(form.data['latitude'], form.data['longitude'], 2009, month)

        months_energy_output = 0
        for day in insolation:
            days_power_output = float(form.data['panel_size'])*float(form.data['panel_rating'])*day[0]/1000 * math.cos(float(form.data['installation_angle'])*math.pi/180)/10000 
            days_energy_output = days_power_output*24
            months_energy_output += days_energy_output
        monthly_energy_output.append(months_energy_output)

    years_energy_output = 0
    for month in monthly_energy_output:
        years_energy_output += month

    output_data = form.data.copy()
    output_data["monthly_energy_output"] = monthly_energy_output
    output_data["years_energy_output"] = years_energy_output
    if form.is_valid(): # All validation rules pass
        return render_to_response('response.html', output_data)


