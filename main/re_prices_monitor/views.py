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

        combined_offers = []
        combined_offers.append(all_offers)

        chart_data = self.prepare_chart_data(combined_offers)

        context = {
            'form': form,
            'latest_offers': latest_offers,
            'chart_data': json.dumps(chart_data)
        }
        return render(request, 'home.html', context)
    

    def post(self, request):
        form = SelectForm(request.POST)
        latest_offers = RealEstateOffer.objects.all().order_by('-id')[:4]
        chart_data = {}

        if form.is_valid():
            # Process the form data
            selected_cities = form.cleaned_data['city']
            selected_market = form.cleaned_data['market']
            selected_data_type = form.cleaned_data['data_type']

            combined_offers = []

            for city in selected_cities:
                for market in selected_market:
                    if selected_data_type[0] == 'Current data':
                        offers = RealEstateOffer.objects.filter(city_name=city).filter(market_type=market)
                        combined_offers.append(offers)
                        
                    else:
                        pass

            chart_data = self.prepare_chart_data(combined_offers)

        context = {
                'form': form,
                'latest_offers': latest_offers,
                'chart_data': json.dumps(chart_data)
            }
        return render(request, 'home.html', context)
    

    def prepare_chart_data(self, combined_offers):
        
        datasets = []
        labels = []

        dataset_colors = ["black", "orange", "grey", 'rgba(75, 192, 192, 1)']

        for num, row in enumerate(combined_offers):
            
            if num == 0:
                labels = [single_row.date for single_row in row]

            datasets.append({
                'label': row[0].city_name + ' - rynek ' + row[0].market_type + ' [PLN/m2]',
                'borderColor': dataset_colors[num],#'#417690',
                'data': [single_row.m2_price for single_row in row]
            })

        return {
            'data': {   
                'labels': labels,
                'datasets': datasets
            }
        }
    