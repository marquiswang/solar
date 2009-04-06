# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html', {})


def calc_payback(request):
    return render_to_response('response.html', {})

