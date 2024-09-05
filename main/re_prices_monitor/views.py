from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .forms import SelectForm
from .models import RealEstateOffer, HistoricRealEstatePrice
import json
import random

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

                    if len(selected_data_type) == 1:
                        if selected_data_type[0] == 'Current data':
                            offers = RealEstateOffer.objects.filter(city_name=city).filter(market_type=market)
                            combined_offers.append(offers)
                            
                        else:
                            offers = HistoricRealEstatePrice.objects.filter(city_name=city).filter(market_type=market)
                            combined_offers.append(offers)
                    else:

                        combined_query = []

                        current_offers = RealEstateOffer.objects.filter(city_name=city).filter(market_type=market).values('date', 'city_name', 'market_type', 'm2_price')
                        historical_offers = HistoricRealEstatePrice.objects.filter(city_name=city).filter(market_type=market).values('date', 'city_name', 'market_type', 'm2_price')
                        
                        combined_query.extend(list(historical_offers))
                        combined_query.extend(list(current_offers))

                        combined_offers.append(combined_query)


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

            if type(row[0]) is dict: #histrorical data combined with current data
                if num == 0:
                    labels = [single_row['date'] for single_row in row]

                datasets.append({
                    'label': row[0]['city_name'] + ' - rynek ' + row[0]['market_type'] + ' [PLN/m2]',
                    'borderColor': dataset_colors[num],#'#417690',
                    'data': [single_row['m2_price'] for single_row in row]
                })
            else:
            
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
    


class GetDataView(View):
    def get(self, request):

        points = 200000
        points2 = 20000
        
        # Wygeneruj listę x_value zawierającą 1000 losowych wartości z zakresu od 0 do 100
        x_value = [random.uniform(0, 100) for _ in range(points)]

        x_value2 = [random.uniform(0, 100) for _ in range(points2)]

        # Wygeneruj listę y_value zawierającą 1000 losowych wartości z zakresu od 0 do 30 oraz od 70 do 100
        y_value = [random.uniform(0, 30) if random.random() < 0.5 else random.uniform(70, 100) for _ in range(points)]

        y_value2 = [random.uniform(0, 10) if random.random() < 0.5 else random.uniform(90, 100) for _ in range(points2)]

        # Połącz listy x_value i y_value w jedną listę par [x, y]
        combined_values = [[x, y] for x, y in zip(x_value, y_value)]

        combined_values2 = [[x, y] for x, y in zip(x_value2, y_value2)]

        result = {
            'data1': combined_values,
            'data2': combined_values2
        }

        #save result like
        return JsonResponse(result, safe=False)
    


class ExtraAxisView(View):
    def get(self, request):
        max_value = request.GET.get('maxValue')
        min_value = request.GET.get('minValue')

        print(max_value, min_value)

        if max_value is None or max_value == '':
            max_value = 90
        else:
            max_value = int(max_value)

        if min_value is None or min_value == '':
            min_value = 10
        else:
            min_value = int(min_value)

        points2 = 20000

        print(max_value, min_value)
        

        x_value2 = [random.uniform(0, 100) for _ in range(points2)]

        y_value2 = [random.uniform(0, min_value) if random.random() < 0.5 else random.uniform(max_value, 100) for _ in range(points2)]


        combined_values2 = [[x, y] for x, y in zip(x_value2, y_value2)]

        result = {
            'data2': combined_values2
        }

        #save result like
        return JsonResponse(result, safe=False)
    

