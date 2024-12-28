from django.urls import path

from . import views as cars_views


urlpatterns = [
    path('create/', cars_views.CreateAnnouncementAPIView.as_view()),
    path('brands/', cars_views.ListBrandAPIView.as_view()),
    path('models/', cars_views.ListModelAPIView.as_view()),
    path('rooftype/', cars_views.ListRoofTypeAPIView.as_view()),
    path('color/', cars_views.ListColorAPIView.as_view()),
    path('fueltype/', cars_views.ListFuelTypeAPIView.as_view()),
    path('enginecapacity/', cars_views.ListEngineCapacityAPIView.as_view()),
    path('forcountry/', cars_views.ListForCountryAPIView.as_view()),
    path('carsupply/', cars_views.ListCarSupplyAPIView.as_view()),
    path('gearbox/', cars_views.ListGearBoxAPIView.as_view()),
]