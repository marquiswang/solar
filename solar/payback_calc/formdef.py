from django import forms

class SystemForm(forms.Form):
    peak_power_output = forms.IntegerField()
    peak_power_output.label = "Peak power output (W)"
    
    installation_price = forms.DecimalField(decimal_places=2)
    installation_price.label = "Installation price"

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

    def month_data(self):
        answer = []
        for i in ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", \
                  "sep", "oct", "nov", "dec"]
            answer += [(self.cleaned_data[i+"_bill"], self.cleaned_data[i+"_usage"])]
        return answer
