from django import forms

class SystemForm(forms.Form):
    peak_power_output = forms.IntegerField()
    peak_power_output.label = "Peak power output (W)"
    
    installation_price = forms.FloatField()
    installation_price.label = "Installation price"

class LocationForm(forms.Form):
    latitude = forms.DecimalField(required=False, max_digits=7, decimal_places=4)
    longitude = forms.DecimalField(required=False, max_digits=7, decimal_places=4)
    city = forms.CharField(required=False)
    state = forms.ChoiceField(required=False)
    state.choices =  \
        [('AL',	'Alabama'),
        ('AK',	'Alaska'),
        ('AZ',	'Arizona'),
        ('AR',	'Arkansas'),
        ('CA',	'California'),
        ('CO',	'Colorado'),
        ('CT',	'Connecticut'),
        ('DE',	'Delaware'),
        ('DC',	'District of Columbia'),
        ('FL',	'Florida'),
        ('GA',	'Georgia'),
        ('HI',	'Hawaii'),
        ('ID',	'Idaho'),
        ('IL',	'Illinois'),
        ('IN',	'Indiana'),
        ('IA',	'Iowa'),
        ('KS',	'Kansas'),
        ('KY',	'Kentucky'),
        ('LA',	'Louisiana'),
        ('ME',	'Maine'),
        ('MD',	'Maryland'),
        ('MA',	'Massachusetts'),
        ('MI',	'Michigan'),
        ('MN',	'Minnesota'),
        ('MS',	'Mississippi'),
        ('MO',	'Missouri'),
        ('MT',	'Montana'),
        ('NE',	'Nebraska'),
        ('NV',	'Nevada'),
        ('NH',	'New Hampshire'),
        ('NJ',	'New Jersey'),
        ('NM',	'New Mexico'),
        ('NY',	'New York'),
        ('NC',	'North Carolina'),
        ('ND',	'North Dakota'),
        ('OH',	'Ohio'),
        ('OK',	'Oklahoma'),
        ('OR',	'Oregon'),
        ('PA',	'Pennsylvania'),
        ('RI',	'Rhode Island'),
        ('SC',	'South Carolina'),
        ('SD',	'South Dakota'),
        ('TN',	'Tennessee'),
        ('TX',	'Texas'),
        ('UT',	'Utah'),
        ('VT',	'Vermont'),
        ('VA',	'Virginia'),
        ('WA',	'Washington'),
        ('WV',	'West Virginia'),
        ('WI',	'Wisconsin'),
        ('WY',	'Wyoming')]
    
    zip_code = forms.CharField(required=False, max_length=5)
    zip_code.label = "ZIP"

class CostsForm(forms.Form):
    avg_price = forms.FloatField()

