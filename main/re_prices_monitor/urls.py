from django.urls import path

from .views import HomeView, GetDataView, ExtraAxisView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('get-data/', GetDataView.as_view(), name='get_data'),
    path('extra-axis/', ExtraAxisView.as_view(), name='extra_axis'),
]