from django import forms

class SolarForm(forms.Form):
    # first part
    number_of_panels = forms.IntegerField()
    panel_size = forms.FloatField()
    installation_angle = forms.FloatField()
    price_per_panel = forms.FloatField()
    panel_rating = forms.FloatField()

    number_of_panels.label = "Number of panels"
    panel_size.label = "Panel size (square centimeters)"
    installation_angle.label = "Installation angle"
    price_per_panel.label = "Price per panel"
    panel_rating.label = "Panel rating (Kw per square meter)"

    # coords
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    
    avg_price = forms.FloatField()

