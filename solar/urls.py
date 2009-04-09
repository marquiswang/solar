from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^$', 'solar.payback_calc.views.index'),
    (r'^calc_payback/', 'solar.payback_calc.views.calc_payback'),
    #(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/day/solar2009/trunk/solar/templates/payback_calc'})

    

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
)
