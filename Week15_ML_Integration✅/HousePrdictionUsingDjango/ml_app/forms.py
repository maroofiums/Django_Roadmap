from django import forms

class HousePredictionForm(forms.Form):
    area = forms.IntegerField(label='Area (in sq ft)')
    rooms = forms.IntegerField(label='Number of Rooms')

