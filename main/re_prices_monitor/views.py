from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import SelectForm

# Create your views here.


class HomeView(View):
    def get(self, request):
        form = SelectForm()
        return render(request, 'home.html', {'form': form})
    

    def post(self, request):
        form = SelectForm(request.POST)
        if form.is_valid():
            # Process the form data
            selected_cities = form.cleaned_data['city']
            selected_market = form.cleaned_data['market']
            selected_data_type = form.cleaned_data['data_type']
            return render(request, 'home.html', {'form': form})
        return render(request, 'home.html', {'form': form})
