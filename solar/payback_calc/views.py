from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    """
        This is a stub.  When this function is called, the main page of the
        payback calculator should load.  templates/index.html should have
        the form.
    """
    return render_to_response('index.html', {})


def calc_payback(request):
    """
        This is a stub for rendering the response to the form in index.html.
        calc_payback should handle handing the information from the response
        to the relevant logic and should assemble the response into a response
        using the response.html template at templates/response.html.
    """
    return render_to_response('response.html', {})
