from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import SelectForm
from .models import RealEstateOffer

# Create your views here.


class HomeView(View):
    def get(self, request):
        form = SelectForm()
        latest_offers = RealEstateOffer.objects.all().order_by('-id')[:4]
        return render(request, 'home.html', {'form': form, 'latest_offers': latest_offers})
    

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
