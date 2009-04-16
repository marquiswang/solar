from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'solar.payback_calc.views.index'),
    (r'^calc_payback/', 'solar.payback_calc.views.calc_payback'),
)
