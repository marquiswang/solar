from django import forms

class SolarForm(forms.Form):
    # first part
    number_of_panels = forms.IntegerField()
    panel_size = forms.FloatField()
    installation_angle = forms.FloatField()
    price_per_panel = forms.FloatField()
    panel_efficiency = forms.FloatField()

    # coords
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    
    avg_price = forms.FloatField()

