from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from formdef import SolarForm

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
        if form.is_valid(): # All validation rules pass
            
    return render_to_response('response.html', {})
