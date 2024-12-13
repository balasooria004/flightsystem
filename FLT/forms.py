from django import forms
from .models import FLIGHT

class AddFlight(forms.ModelForm):
    class Meta:
        model = FLIGHT
        fields = ['flt_name', 'flt_from', 'flt_to', 'flt_duration']


class UpdateFlight(forms.ModelForm):
    class Meta:
        model = FLIGHT
        fields = ['flt_from', 'flt_to', 'flt_duration']

class GetFlightId(forms.Form):
    flt_id = forms.IntegerField(label="Enter flight id : ")