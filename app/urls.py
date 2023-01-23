from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("events/", views.eventList, name="eventList")
]
