Solar Panel Installation Planner (SPIP)                 HMC CS121 Spring 2009

0. Authors

Samuel Just
Marquis Wang
Dmitriy Yakovlev

1. Code Layout

SPIP consists of a single form, the results of which are processed and then displayed on an output page. Due to the way Django works, the code that supports all of this is distributed among many different files. This reference outlines the code that runs the specific project, not Django in general. 

solar2009/
    django.wsgi : configuration file for Django
    monitor.py : fix for a caching issue. 

solar2009/docs/
    contains project documentation
    
solar2009/resources/
    contains the outside source files we used in this project. See External
    Resources section for a detailed breakdown of contents.

solar2009/solar/
    settings.py : Django project settings
    urls.py : Django rewrite rules for form locations

solar2009/solar/media/
    contains directories css/ and js/, which hold the css and js used by SPIP

solar2009/solar/payback_calc/
    payback_lib.py : support library for view that calculates the projection
    formdef.py : definitions for the input form subsections
    hostip.py : support library for ip-location database
    models.py : Django-generated file that defines database access functions
    srlocat_wrapper.py : wrapper for SRLOCAT.F, for calculating insolation data
    views.py : functions for generating the input form, response, and error page
    
solar2009/solar/templates/payback_calc/
    base.html : template-template, defines outline that other templates extend
    error.html : template for errors 
    index.html : template that defines the way the input form view looks
    response.html : template that defines the way the response view looks
    
2. External Resources 

(in solar2009/resources)

2007avgprices.txt
    Average state electricity prices for 2007.  
    Retrieved from _____
    
22yr_swv_dwn.gz/txt
    Empirical insolation data from NASA SSE
    Retrieved from http://eosweb.larc.nasa.gov/sse/
    
hostip_current.sql.tar.gz
    ip geolocation database, maps IPs to latitude and longitude information.
    Retrieved from http://www.hostip.info/

SRLOCAT.F
    Purely geometry-based insolation calculator in Fortran. 
    Retrieved from http://aom.giss.nasa.gov/srlocat.html
    
zipcode.sql
    zip code <--> lat/long database <--> city, state information
    Retrieved from http://scripts.ringsworld.com/calculators/zipcode-1.1.0/sql/zip-code-2.sql.html
    
(in solar2009/solar/media/js)

jquery*.js
    jQuery, javascript effects library
    
jscharts.js
    jsCharts, javascript chart creation library
    
livevalidation*.js
    LiveValidation, javascript clientside form validation library
    

    
3. Roadmap for the Future


hmm.