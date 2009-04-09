from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from formdef import *
from solar.payback_calc.srlocat_wrapper import avg_sunlight
from solar.payback_calc.hostip import *
from solar.payback_calc.avg_cost import avg_cost

import datetime

def index(request):
    """
        This is a stub.  When this function is called, the main page of the
        payback calculator should load.  templates/index.html should have
        the form.
    """
    city, state, zip_code, lat, lng = ip_to_location(request.META.get('REMOTE_ADDR'))
    
    system_form = SystemForm()
    location_form = LocationForm(initial = \
        {   'city' : city, 
            'state' : state, 
            'zip_code' : zip_code, 
            'latitude' : lat, 
            'longitude' : lng
        })
    costs_form = CostsForm()
    return render_to_response('index.html', {'system_form': system_form, 'location_form': location_form, 'costs_form': costs_form})


def calc_payback(request):
    """
        This is a stub for rendering the response to the form in index.html.
        calc_payback should handle handing the information from the response
        to the relevant logic and should assemble the response into a response
        using the response.html template at templates/response.html.
    """
     # Check to make sure a form has been submitted...
    if request.method != 'POST':
        return render_to_response('error.html', {'error_message' : 'No form submitted'})

	# Bind forms to the POST data
    system_form = SystemForm(request.POST)
    location_form = LocationForm(request.POST)
    costs_form = CostsForm(request.POST)
    
    # All validation rules pass
    if not system_form.is_valid() or not location_form.is_valid() or not costs_form.is_valid():
        return render_to_response('error.html', {'error_message' : 'Invalid form'})
    
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
        city, state, lat, lng = zip_to_location(zip_code)
    else:
        return render_to_response('error.html', {
            'error_message': "You didn't select a location choice.",
        })
    
    # Determine a list of monthly (payed, used)
    cost_per_month = []
    costs_choice = request.POST['costs_choice']
    
    if (costs_choice == "averages" and loc_choice != "lat_lng"):
        cost_per_month = [avg_cost(state)]*12
    elif (costs_choice == "specified"):
        cost_per_month = costs_form.month_data()
    else:
        return render_to_response('error.html', {'error_message' : 'You didn\'t select a cost choice.'})

    # Calculate one year of energy savings
    peak_power_output = system_form.cleaned_data['peak_power_output']
    installation_price = system_form.cleaned_data['installation_price']
    
    i = 1
    yearly_amount_saved = 0
    for (cost, usage) in cost_per_month:
        yearly_amount_saved += (avg_sunlight(lat, lng, today.year-1, i, peak_power_output)/1000)\
            * (float(cost)/float(usage))
        i+=1

    # Calculate payback time
    payback_time = float(installation_price) / yearly_amount_saved
    
    output_data = {}
    output_data.update(system_form.cleaned_data)
    output_data.update(location_form.cleaned_data)
    output_data["loc_choice"] = loc_choice
    output_data["lat_str"] = str("%.4f" % lat)+"N" if lat > 0 else str("%.4f" % -lat)+"S"
    output_data["lng_str"] = str("%.4f" % lng)+"E" if lng > 0 else str("%.4f" % -lng)+"W"
    output_data["savings"] = str("%.2f" % yearly_amount_saved)
    output_data["payback_time"] = str("%.4f" % payback_time)
    
    if loc_choice != "lat_lng":
        output_data["city"] = city
        output_data["state"] = state
    
    return render_to_response('response.html', output_data)

    

