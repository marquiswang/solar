from django import forms

class SolarForm(forms.Form):
    # first part
    # number_of_panels = forms.IntegerField()
    # number_of_panels.label = "Number of panels"
    # 
    # panel_size = forms.FloatField()
    # panel_size.label = "Panel size (square centimeters)"
    # 
    # installation_angle = forms.FloatField()
    # installation_angle.label = "Installation angle"
    # 
    # price_per_panel = forms.FloatField()
    # price_per_panel.label = "Price per panel"
    # 
    # panel_rating = forms.FloatField()
    # panel_rating.label = "Panel rating (Kw per square meter)"

    peak_power_output = forms.FloatField()
    peak_power_output.label = "Peak power output (W)"
    
    installation_price = forms.FloatField()
    installation_price.label = "Installation price"

    # coords
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    
    avg_price = forms.FloatField()

