from django import forms
from django_select2.forms import Select2MultipleWidget, Select2Widget


class SelectForm(forms.Form):
    OPTIONS = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]

    city = forms.MultipleChoiceField(
        choices=OPTIONS, 
        label='Select city', 
        widget=Select2MultipleWidget(attrs={'id': 'id_city'}),
        initial=['option1'])
    
    market = forms.MultipleChoiceField(
        choices=OPTIONS, 
        label='Select market',
        widget=Select2MultipleWidget(attrs={'id': 'id_market'}),
        initial=['option1'])
    
    data_type = forms.MultipleChoiceField(
        choices=OPTIONS, 
        label='Select data type',
        widget=Select2MultipleWidget(attrs={'id': 'id_data_type'}),
        initial=['option1'])