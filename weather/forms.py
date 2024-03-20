from django import forms

class WeatherForm(forms.Form):
    temperature = forms.FloatField(label='Temperature')
    date = forms.DateTimeField(label='Date')
    city = forms.CharField(label='City', required=False)
    atmosphericPressure = forms.CharField(label='Atmospheric Pressure', required=False)
    humidity = forms.CharField(label='Humidity', required=False)
    weather = forms.CharField(label='Weather', required=False)
