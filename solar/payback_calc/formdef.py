# This Python file uses the following encoding: utf-8
from django import forms

class SystemForm(forms.Form):
    peak_power_output = forms.IntegerField()
    peak_power_output.label = "Peak power output (W)"
    peak_power_output_explanation = "Explanation for peak power output!"
    
    installation_price = forms.DecimalField(decimal_places=2)
    installation_price.label = "Installation price ($)"
    installation_price_explanation = "Explanation for installation price!"

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
    avg_explanation = "Average price explanation!"
    spec_explanation = "Specified price explanation!"
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
    buyback_price.label = "Buyback price ($)"
    buyback_price_explanation = "Buyback price explanation!"
    
    inflation_rate = forms.DecimalField(required=False)
    inflation_rate.label = "Inflation rate (%)"
    inflation_rate_explanation = "Inflation rate explanation!"
    
    tier_explanation = "Tiered pricing explanation!"
    tier_price_label = "Tier price (¢/Wh)"
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
    
