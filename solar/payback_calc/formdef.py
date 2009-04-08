from django import forms

class SystemForm(forms.Form):
    peak_power_output = forms.FloatField()
    peak_power_output.label = "Peak power output (W)"
    
    installation_price = forms.FloatField()
    installation_price.label = "Installation price"

class LocationForm(forms.Form):
    latitude = forms.FloatField()
    longitude = forms.FloatField()

class CostsForm(forms.Form):
    avg_price = forms.FloatField()

