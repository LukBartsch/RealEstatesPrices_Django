from django import forms
from django_select2.forms import Select2MultipleWidget, Select2Widget
from .models import RealEstateOffer


class SelectForm(forms.Form):

    DATA_TYPE_OPTIONS = [
        ('Current data', 'Current data'),
        ('Historical data', 'Historical data'),
    ]

    city = forms.MultipleChoiceField(
        label='Select city', 
        widget=Select2MultipleWidget(attrs={'id': 'id_city'}),
        initial=['Wrocław'])
    
    market = forms.MultipleChoiceField(
        label='Select market',
        widget=Select2MultipleWidget(attrs={'id': 'id_market'}),
        initial=['pierwotny'])
    
    data_type = forms.MultipleChoiceField(
        choices=DATA_TYPE_OPTIONS, 
        label='Select data type',
        widget=Select2MultipleWidget(attrs={'id': 'id_data_type'}),
        initial=['Current data'])
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].choices = self.get_city_choices()
        self.fields['market'].choices = self.get_market_choices()

    def get_city_choices(self):
        cities = RealEstateOffer.objects.values_list('city_name', flat=True).distinct()
        return [(city, city) for city in cities]

    def get_market_choices(self):
        markets = RealEstateOffer.objects.values_list('market_type', flat=True).distinct()
        return [(market, market) for market in markets]