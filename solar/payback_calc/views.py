from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from formdef import SolarForm
from solar.payback_calc.srlocat_wrapper import srlocat

import datetime

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
     # Check to make sure a form has been submitted...
    if request.method != 'POST':
        return render_to_response('error.html', {})

	# Bind form to the POST data
    form = SolarForm(request.POST)

    # All validation rules pass
    if not form.is_valid():
        return render_to_response('error.html', {})

    form.clean()
    
    one_day = datetime.timedelta(days=1)
    today = datetime.date.today()
    expected_lifetime = datetime.timedelta(weeks=1)
    end_of_life = today + expected_lifetime
    
    # Calculate upcoming energy output
    energy_output = []
    
    day = today
    while day < end_of_life:
        insolation = srlocat(form.cleaned_data['latitude'], \
                             form.cleaned_data['longitude'], day.year, day.month, day.day)
        
        days_power_output = form.cleaned_data['peak_power_output'] * insolation[0] / 1000.0
        days_energy_output = days_power_output * 24 / 1000
        
        days_info = {}
        days_info['day'] = day.strftime("%m/%d/%y")
        days_info['energy_output'] = days_energy_output
        
        energy_output.append( days_info ) 
        day += one_day

    output_data = form.cleaned_data.copy()
    output_data["energy_output"] = energy_output
    
    return render_to_response('response.html', output_data)

    

