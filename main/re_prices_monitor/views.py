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
            city = form.cleaned_data['city']
            return HttpResponse(f'You selected {city}')
        return render(request, 'home.html', {'form': form})