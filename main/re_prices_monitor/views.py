from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .forms import SelectForm
from .models import RealEstateOffer
import json

# Create your views here.


class HomeView(View):
    def get(self, request):
        form = SelectForm()
        all_offers = RealEstateOffer.objects.filter(city_name='Wrocław').filter(market_type='pierwotny')
        latest_offers = RealEstateOffer.objects.all().order_by('-id')[:4]


        chart_data = {
            'data': {
                'labels': [item.date for item in all_offers],
                'datasets': [{
                    'label': 'Wrocław - rynek pierwotny [PLN/m2]',
                    "borderColor": "#417690",
                    'data': [item.m2_price for item in all_offers],
                }]
            },
        }

        context = {
            'form': form,
            'latest_offers': latest_offers,
            'chart_data': json.dumps(chart_data)
        }
        return render(request, 'home.html', context)
    

    def post(self, request):
        form = SelectForm(request.POST)
        latest_offers = RealEstateOffer.objects.all().order_by('-id')[:4]
        if form.is_valid():
            # Process the form data
            selected_cities = form.cleaned_data['city']
            selected_market = form.cleaned_data['market']
            selected_data_type = form.cleaned_data['data_type']
            return render(request, 'home.html', {'form': form, 'latest_offers': latest_offers})
        return render(request, 'home.html', {'form': form, 'latest_offers': latest_offers})
