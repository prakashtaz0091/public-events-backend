from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("events/", views.eventList, name="eventList"),
    path("events/district/<str:district>", views.filterByDistrict, name="filterByDistrict"),
    path("events/municipality/<str:municipality>", views.filterByMunicipality, name="filterByMunicipality"),
    path("events/local-address/<str:local_address>", views.filterByLocalAddress, name="filterByLocalAddress"),
]
