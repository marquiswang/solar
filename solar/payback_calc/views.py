from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from formdef import *
from solar.payback_calc.hostip import *
from solar.payback_calc.payback_lib import *

import datetime

def index(request):
    """
        When this function is called, the main page of the
        payback calculator should load.  templates/index.html should have
        the form.
    """
    initial_system   = {}
    initial_location = {}
    initial_costs    = {}
    initial_advanced = {}
    saved_data = ""
    loc_choice = "city_state"
    costs_choice = "averages"

    advanced_control = ""
    
    # Get saved state data if exists
    if 'saved_data' in request.session:
        saved_data = request.session['saved_data']
        costs_choice = request.session['costs_choice']
        loc_choice = request.session['loc_choice']
        advanced_control = request.session['advanced_control']
        
        initial_system = {
            'peak_power_output' : request.session['peak_power_output'], 
            'installation_price' : request.session['installation_price']
            }
        initial_location = {
            'city' : request.session['city'], 
            'state' : request.session['state'], 
            'zip_code' : request.session['zip_code'], 
            'latitude' : request.session['latitude'], 
            'longitude' : request.session['longitude']
            }
        initial_costs = {
            'jan_bill' : request.session['jan_bill'],
            'jan_usage': request.session['jan_usage'],
            'feb_bill' : request.session['feb_bill'],
            'feb_usage': request.session['feb_usage'],
            'mar_bill' : request.session['mar_bill'],
            'mar_usage': request.session['mar_usage'],
            'apr_bill' : request.session['apr_bill'],
            'apr_usage': request.session['apr_usage'],
            'may_bill' : request.session['may_bill'],
            'may_usage': request.session['may_usage'],
            'jun_bill' : request.session['jun_bill'],
            'jun_usage': request.session['jun_usage'],
            'jul_bill' : request.session['jul_bill'],
            'jul_usage': request.session['jul_usage'],
            'aug_bill' : request.session['aug_bill'],
            'aug_usage': request.session['aug_usage'],
            'sep_bill' : request.session['sep_bill'],
            'sep_usage': request.session['sep_usage'],
            'oct_bill' : request.session['oct_bill'],
            'oct_usage': request.session['oct_usage'],
            'nov_bill' : request.session['nov_bill'],
            'nov_usage': request.session['nov_usage'],
            'dec_bill' : request.session['dec_bill'],
            'dec_usage': request.session['dec_usage']
        }
        initial_advanced = {
            'buyback_price' : request.session['buyback_price'],
            'inflation_rate': request.session['inflation_rate'],
            'years_projection': request.session['years_projection'],
            'tier_price_1'  : request.session['tier_price_1'],
            'tier_limit_1'  : request.session['tier_limit_1'],
            'tier_price_2'  : request.session['tier_price_2'],
            'tier_limit_2'  : request.session['tier_limit_2'],
            'tier_price_3'  : request.session['tier_price_3'],
            'tier_limit_3'  : request.session['tier_limit_3'],
            'tier_price_4'  : request.session['tier_price_4'],
            'tier_limit_4'  : request.session['tier_limit_4'],
            'tier_price_5'  : request.session['tier_price_5'],
            'tier_limit_5'  : request.session['tier_limit_5'],
            'tier_price_6'  : request.session['tier_price_6'],
            'tier_limit_6'  : request.session['tier_limit_6'],
        }
    else:
        city, state, zip_code, lat, lng = ip_to_location(request.META.get('REMOTE_ADDR'))
        initial_location = {
            'city' : city, 
            'state' : state, 
            'zip_code' : zip_code, 
            'latitude' : lat, 
            'longitude' : lng
        }
        initial_advanced = {
            'buyback_price' : 0,
            'inflation_rate' : 6,
            'years_projection' : 40,
        }

    system_form = SystemForm(initial = initial_system)
    location_form = LocationForm(initial = initial_location)
    costs_form = CostsForm(initial = initial_costs)
    advanced_form = AdvancedForm(initial = initial_advanced)
    return render_to_response('index.html', {
        'system_form': system_form, 
        'location_form': location_form, 
        'costs_form': costs_form,
        'advanced_form': advanced_form,
        'costs_choice': costs_choice,
        'loc_choice' : loc_choice,
        'advanced_control' : advanced_control,
        'saved_data' : saved_data
        })

def calc_payback(request):
    """
        This is a function for rendering the response to the form in index.html.
        calc_payback should handle handing the information from the response
        to the relevant logic and should assemble the response into a response
        using the response.html template at templates/response.html.
    """
    def debug(err):
        erroroutput = open("/home/sam/solar2009/solar/payback_calc/debug.err", 'a')
        erroroutput.write(err+"\n")
        erroroutput.close()

     # Check to make sure a form has been submitted...
    if request.method != 'POST':
        return render_to_response('error.html', {'error_message' : 'No form submitted'})

	# Bind forms to the POST data
    system_form = SystemForm(request.POST)
    location_form = LocationForm(request.POST)
    costs_form = CostsForm(request.POST)
    advanced_form = AdvancedForm(request.POST)

    # All validation rules pass
    if not system_form.is_valid() or not location_form.is_valid() or not costs_form.is_valid() or not advanced_form.is_valid():
        return render_to_response('error.html', {'error_message' : 'Invalid form'})
    
    # Determine user's location
    loc_choice = request.POST['loc_choice']
    if loc_choice == "lat_lng":
        lat = location_form.cleaned_data['latitude']
        lng = location_form.cleaned_data['longitude']
    elif loc_choice == "city_state":
        city = location_form.cleaned_data['city']
        state = location_form.cleaned_data['state']
        citydata = city_to_latlng(city, state)
        if citydata == False:
             return render_to_response('error.html', {'error_message' : city + ", "+state + " not found"})
        lat, lng = citydata
    elif loc_choice == "zip_code":
        zip_code = location_form.cleaned_data['zip_code']
        zipdata = zip_to_location(zip_code)
        if zipdata == False:
             return render_to_response('error.html', {'error_message' : "Zip code "+ zip_code + " not found"})
        city, state, lat, lng = zipdata
    else:
        return render_to_response('error.html', {
            'error_message': "You didn't select a location choice.",
        })
    
    # Determine a list of monthly (payed, used) based on costs_choice
    cost_per_month = []
    costs_choice = request.POST['costs_choice']
    
    if (costs_choice == "averages" and loc_choice == "lat_lng"):
        return render_to_response('error.html', {'error_message' : \
        'Location averages with latitude and longitude are not supported.  Please enter a City/State or ZIP.'})

    if (costs_choice == "averages"):
        cost_per_month = [avg_cost(state)]*12
    elif (costs_choice == "specified"):
        cost_per_month = costs_form.month_data()
    else:
        return render_to_response('error.html', {'error_message' : \
            'Please select either Location Averages or Power Bill data.'})
    
    peak_power_output = system_form.cleaned_data['peak_power_output']
    installation_price = system_form.cleaned_data['installation_price']
    
    # input stage is over, calculations begin

    tiers = 0
    buyback = 0
    inf_rate = 1.06
    years_projection = 40
    
    # process advanced input variables if they are available
    if 'advanced_control' in request.POST:
        if (advanced_form.cleaned_data['buyback_price'] != None):
            buyback = float(advanced_form.cleaned_data['buyback_price'])
        if (advanced_form.cleaned_data['inflation_rate'] != None):
            inf_rate = 1 + float(advanced_form.cleaned_data['inflation_rate'])*0.01
        if (advanced_form.cleaned_data['tier_price_1'] != None): 
            tiers = advanced_form.tier_data()
        if (advanced_form.cleaned_data['years_projection'] != None):
            years_projection = float(advanced_form.cleaned_data['years_projection'])
    
    # calculate the savings in the first month   
    today = datetime.date.today()     
    savings_per_month = calc_monthly_savings(cost_per_month, lat, lng, today,\
                                              peak_power_output, tiers, buyback, debug = debug)

    yearly_amount_saved = reduce(lambda x,(_,y):x+float(y), [0]+savings_per_month)
        
    # calculate payback time, taking inflation into account (set inf_rate to 0 for no inflation)
    payback_time, graph_entries = \
        calc_infl_payback_time(installation_price, savings_per_month, inf_rate, years_projection)

    payback_years = int(payback_time)
    payback_months = int(12*(payback_time - int(payback_time)))
	

    # calculations done, format output data
    output_data = {}
    output_data.update(system_form.cleaned_data)
    output_data.update(location_form.cleaned_data)
    output_data["loc_choice"] = loc_choice
    output_data["lat_str"] = str("%.4f" % lat)+"N" if lat > 0 else str("%.4f" % -lat)+"S"
    output_data["lng_str"] = str("%.4f" % lng)+"E" if lng > 0 else str("%.4f" % -lng)+"W"
    output_data["savings"] = str("%.2f" % yearly_amount_saved)
    output_data["payback_time"] = payback_time
    output_data["payback_years"] = payback_years
    output_data["payback_months"] = payback_months
    output_data["payoff_entries"] = graph_entries
    
    if loc_choice != "lat_lng":
        output_data["city"] = city
        output_data["state"] = state

    # If necessary, save in session cookie all data given.
    if ('save' in request.POST):
        request.session["saved_data"] = "checked"
        request.session["costs_choice"] = costs_choice
        request.session["loc_choice"] = loc_choice
        request.session["advanced_control"] = advanced_control
        
        for data_pt in system_form.cleaned_data:
            request.session[data_pt] = system_form.cleaned_data[data_pt]
        for data_pt in location_form.cleaned_data:
            request.session[data_pt] = location_form.cleaned_data[data_pt]
        for data_pt in costs_form.cleaned_data:
            request.session[data_pt] = costs_form.cleaned_data[data_pt]
        for data_pt in advanced_form.cleaned_data:
            request.session[data_pt] = advanced_form.cleaned_data[data_pt]
    elif 'saved_data' in request.session:
        del request.session["saved_data"]
        
    # come up with an explanation for the user for the calculation
    user_explanation = "Your payback period was computed using "
    if costs_choice == "averages":
        user_explanation+="average price information from your state ("
        user_explanation+=str("%.2f" % (cost_per_month[0][0]/cost_per_month[0][1]))
        user_explanation+=" $/kWh) "
    else:
        user_explanation+="your power bill information over 12 months"
    if tiers:
        user_explanation+=" along with tiered pricing information.  "
    else:
        user_explanation+=".  "
    if inf_rate != 0:
        user_explanation+="The calculation also assumes that your "
        user_explanation+="power costs will increase at an annual"
        user_explanation+=" rate of "+str((inf_rate-1)*100)+"%."
    output_data["user_explanation"] = user_explanation

    return render_to_response('response.html', output_data)

    

