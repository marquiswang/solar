from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from formdef import SolarForm
from solar.payback_calc.srlocat_wrapper import srlocat

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

    if (not form.is_valid()): # All validation rules pass
        return render_to_response('error.html', {})

    form.clean()
    
    # Calculate upcoming energy output
    monthly_energy_output = []

    for m in range(0, 12):
        month = m+1
        insolation = srlocat(form.data['latitude'], \
                             form.data['longitude'], 2009, month)

        months_energy_output = 0
        for day in insolation:
            days_power_output = form.data['peak_power_output']*day[0]/1000  
            days_energy_output = days_power_output*24
            months_energy_output += days_energy_output
        monthly_energy_output.append(months_energy_output)

    years_energy_output = 0
    for month in monthly_energy_output:
        years_energy_output += month

    output_data = form.data.copy()
    output_data["monthly_energy_output"] = monthly_energy_output
    output_data["years_energy_output"] = years_energy_output
    
     # All validation rules pass
    if form.is_valid():
        return render_to_response('response.html', output_data)
    return render_to_response('response.html', output_data)

    

