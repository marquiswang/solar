# This Python file uses the following encoding: utf-8
from django import forms

class SystemForm(forms.Form):
    peak_power_output = forms.IntegerField()
    peak_power_output.label = "Peak power output (W)"
    peak_power_output_explanation = \
        """A solar panel system is rated for a certain peak power output, which is the expected power 
        output of the system under optimal conditions."""
    
    installation_price = forms.DecimalField(decimal_places=2)
    installation_price.label = "Installation price ($)"
    installation_price_explanation = \
        """The cost of installing a solar panel system varies depending on the type of solar panel, 
        the house on which it is being installed, and more. To get an accurate cost estimate, you 
        should get a quote from an expert. This value should be your total outlay after all government
        rebates and tax benefits."""

class LocationForm(forms.Form):
    latitude = forms.DecimalField(required=False, max_digits=7, decimal_places=4)
    longitude = forms.DecimalField(required=False, max_digits=7, decimal_places=4)
    city = forms.CharField(required=False)
    state = forms.ChoiceField(required=False)
    state.choices =  \
        [('',''),
        ('AL','AL'),
        ('AK','AK'),
        ('AZ','AZ'),
        ('AR','AR'),
        ('CA','CA'),
        ('CO','CO'),
        ('CT','CT'),
        ('DE','DE'),
        ('DC','DC'),
        ('FL','FL'),
        ('GA','GA'),
        ('HI','HI'),
        ('ID','ID'),
        ('IL','IL'),
        ('IN','IN'),
        ('IA','IA'),
        ('KS','KS'),
        ('KY','KY'),
        ('LA','LA'),
        ('ME','ME'),
        ('MD','MD'),
        ('MA','MA'),
        ('MI','MI'),
        ('MN','MN'),
        ('MS','MS'),
        ('MO','MO'),
        ('MT','MT'),
        ('NE','NE'),
        ('NV','NV'),
        ('NH','NH'),
        ('NJ','NJ'),
        ('NM','NM'),
        ('NY','NY'),
        ('NC','NC'),
        ('ND','ND'),
        ('OH','OH'),
        ('OK','OK'),
        ('OR','OR'),
        ('PA','PA'),
        ('RI','RI'),
        ('SC','SC'),
        ('SD','SD'),
        ('TN','TN'),
        ('TX','TX'),
        ('UT','UT'),
        ('VT','VT'),
        ('VA','VA'),
        ('WA','WA'),
        ('WV','WV'),
        ('WI','WI'),
        ('WY','WY')]

    
    zip_code = forms.CharField(required=False, max_length=5)
    zip_code.label = "ZIP"

class CostsForm(forms.Form):
    avg_explanation = "Use the average power cost and usage data for your state (as of 2007)."
    spec_explanation = \
        """If you have your own power bill available, you can get more personalized data by
        using your own monthly power usage and cost data for the calculations."""
    jan_bill  = forms.DecimalField(required=False, decimal_places=2)
    jan_usage = forms.IntegerField(required=False)
    feb_bill  = forms.DecimalField(required=False, decimal_places=2)
    feb_usage = forms.IntegerField(required=False)
    mar_bill  = forms.DecimalField(required=False, decimal_places=2)
    mar_usage = forms.IntegerField(required=False)
    apr_bill  = forms.DecimalField(required=False, decimal_places=2)
    apr_usage = forms.IntegerField(required=False)
    may_bill  = forms.DecimalField(required=False, decimal_places=2)
    may_usage = forms.IntegerField(required=False)
    jun_bill  = forms.DecimalField(required=False, decimal_places=2)
    jun_usage = forms.IntegerField(required=False)
    jul_bill  = forms.DecimalField(required=False, decimal_places=2)
    jul_usage = forms.IntegerField(required=False)
    aug_bill  = forms.DecimalField(required=False, decimal_places=2)
    aug_usage = forms.IntegerField(required=False)
    sep_bill  = forms.DecimalField(required=False, decimal_places=2)
    sep_usage = forms.IntegerField(required=False)
    oct_bill  = forms.DecimalField(required=False, decimal_places=2)
    oct_usage = forms.IntegerField(required=False)
    nov_bill  = forms.DecimalField(required=False, decimal_places=2)
    nov_usage = forms.IntegerField(required=False)
    dec_bill  = forms.DecimalField(required=False, decimal_places=2)
    dec_usage = forms.IntegerField(required=False)

    bills = \
    [
    ("January", jan_bill, jan_usage),
    ("February", feb_bill, feb_usage),
    ("March", mar_bill, mar_usage),
    ("April", apr_bill, apr_usage),
    ("May", may_bill, may_usage),
    ("June", jun_bill, jun_usage),
    ("July", jul_bill, jul_usage),
    ("August", aug_bill, aug_usage),
    ("September", sep_bill, sep_usage),
    ("October", oct_bill, oct_usage),
    ("November", nov_bill, nov_usage),
    ("December", dec_bill, dec_usage)
    ]

    def month_data(self):
        answer = []
        for i in ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", \
                  "sep", "oct", "nov", "dec"]:
            answer += [(self.cleaned_data[i+"_bill"], self.cleaned_data[i+"_usage"])]
        return answer
        
class AdvancedForm(forms.Form):
    buyback_price = forms.DecimalField(required=False)
    buyback_price.label = "Net-Metering rate ($/Wh)"
    buyback_price_explanation = \
        """Some utilities offer to buy back excess power generated from a solar panel 
        system at a special rate. If your utility offers such a program, this buyback price (referred to as a Net-Metering rate)
        can be taken into account in the calculations. This rate should be given in
        cents per watt-hour."""
    
    inflation_rate = forms.DecimalField(required=False)
    inflation_rate.label = "Inflation rate (%)"
    inflation_rate_explanation = \
        """Electricity prices do not actually stay the same year after year. This sets the
        rate at which the calculations assume that power costs will rise in the future."""
    
    years_projection = forms.DecimalField(required=False)
    years_projection.label = "Panel Lifetime (yrs)"
    years_projection_explanation = \
        """All solar panels have a lifetime expectancy. This variable sets how far in the 
        future we project the payback progress."""
    
    tier_explanation = \
        """To encourage energy conservation, some utilities offer 'tiered' rate structures, 
        where your cost per kilowatt-hour (kWh) increases as you use more electricity. Such information
        should appear on your monthly power bill, and can be taken into account in the calculations."""
    tier_price_label = "Tier price ($/Wh)"
    tier_limit_label = "Tier limit (Wh)"
    tier_price_1 = forms.DecimalField(required=False)
    tier_limit_1 = forms.IntegerField(required=False)
    tier_price_2  = forms.DecimalField(required=False)
    tier_limit_2 = forms.IntegerField(required=False)
    tier_price_3  = forms.DecimalField(required=False)
    tier_limit_3 = forms.IntegerField(required=False)
    tier_price_4  = forms.DecimalField(required=False)
    tier_limit_4 = forms.IntegerField(required=False)
    tier_price_5  = forms.DecimalField(required=False)
    tier_limit_5 = forms.IntegerField(required=False)
    tier_price_6  = forms.DecimalField(required=False)
    tier_limit_6 = forms.IntegerField(required=False)
    
    tiers = \
    [
    (tier_price_1, tier_limit_1),
    (tier_price_2, tier_limit_2),
    (tier_price_3, tier_limit_3),
    (tier_price_4, tier_limit_4),
    (tier_price_5, tier_limit_5),
    (tier_price_6, tier_limit_6)
    ]
    
    def tier_data(self):
        answer = []
        for i in ['1','2','3','4','5','6']:
            if (self.cleaned_data["tier_price_"+i] == None): # if there's no more tiered pricing info
                break
            answer += [(self.cleaned_data["tier_price_"+i], self.cleaned_data["tier_limit_"+i])]
        return answer
    
