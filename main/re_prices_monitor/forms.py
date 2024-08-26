from django import forms
from django_select2.forms import Select2MultipleWidget, Select2Widget


class SelectForm(forms.Form):
    CITY_OPTIONS = [
        ('Wrocław', 'Wrocław'),
        ('Ostrów Wlkp.', 'Ostrów Wlkp.'),
    ]
    MARKET_OPTIONS = [
        ('pierwotny', 'pierwotny'),
        ('wtorny', 'wtorny'),
    ]

    DATA_TYPE_OPTIONS = [
        ('Current data', 'Current data'),
        ('Historical data', 'Historical data'),
    ]

    city = forms.MultipleChoiceField(
        choices=CITY_OPTIONS, 
        label='Select city', 
        widget=Select2MultipleWidget(attrs={'id': 'id_city'}),
        initial=['Wrocław'])
    
    market = forms.MultipleChoiceField(
        choices=MARKET_OPTIONS, 
        label='Select market',
        widget=Select2MultipleWidget(attrs={'id': 'id_market'}),
        initial=['pierwotny'])
    
    data_type = forms.MultipleChoiceField(
        choices=DATA_TYPE_OPTIONS, 
        label='Select data type',
        widget=Select2MultipleWidget(attrs={'id': 'id_data_type'}),
        initial=['Current data'])