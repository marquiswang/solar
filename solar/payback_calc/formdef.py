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
        [('AL','AL'),
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
    avg_price = forms.FloatField()

