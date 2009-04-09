from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from formdef import *
from solar.payback_calc.srlocat_wrapper import srlocat
from solar.payback_calc.hostip import *

import datetime

def index(request):
    """
        This is a stub.  When this function is called, the main page of the
        payback calculator should load.  templates/index.html should have
        the form.
    """
    system_form = SystemForm()
    
    city, state, zip_code, lat, lng = ip_to_location(request.META.get('REMOTE_ADDR'))
    location_form = LocationForm(initial = \
        {'city' : city, 'state' : state, 'zip_code' : zip_code, 'latitude' : lat, 'longitude' : lng})
    return render_to_response('index.html', {'system_form': system_form, 'location_form': location_form})


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

	# Bind forms to the POST data
    system_form = SystemForm(request.POST)
    location_form = LocationForm(request.POST)
    
    # All validation rules pass
    if not system_form.is_valid() or not location_form.is_valid():
        return render_to_response('error.html', {})
    
    one_day = datetime.timedelta(days=1)
    today = datetime.date.today()
    expected_lifetime = datetime.timedelta(weeks=2)
    end_of_life = today + expected_lifetime
    
    # Determine user's location
    loc_choice = request.POST['loc_choice']
    if loc_choice == "lat_lng":
        lat = location_form.cleaned_data['latitude']
        lng = location_form.cleaned_data['longitude']
    elif loc_choice == "city_state":
        city = location_form.cleaned_data['city']
        state = location_form.cleaned_data['state']
        lat, lng = city_to_latlng(city, state)
    elif loc_choice == "zip_code":
        zip_code = location_form.cleaned_data['zip_code']
        lat,lng = zip_to_latlng(zip_code)
    else:
        return render_to_response('error.html', {
            'error_message': "You didn't select a choice.",
        })
    
    # Calculate upcoming energy output
    peak_power_output = system_form.cleaned_data['peak_power_output']
    energy_output = []
    
    day = today
    while day < end_of_life:
        insolation, zenith_cos = srlocat(lat, lng, day.year, day.month, day.day)
        
        days_power_output = peak_power_output * insolation / 1000.0
        days_energy_output = days_power_output * 24 / 1000
        
        days_info = {}
        days_info['day'] = day.strftime("%m/%d/%y")
        days_info['energy_output'] = days_energy_output
        
        energy_output.append( days_info ) 
        day += one_day

    output_data = {}
    output_data.update(system_form.cleaned_data)
    output_data.update(location_form.cleaned_data)
    output_data["energy_output"] = energy_output
    output_data["loc_choice"] = loc_choice
    output_data["lat_str"] = str("%.4f" % lat)+"N" if lat > 0 else str("%.4f" % -lat)+"S"
    output_data["lng_str"] = str("%.4f" % lng)+"E" if lng > 0 else str("%.4f" % -lng)+"W"
    
    return render_to_response('response.html', output_data)

    

