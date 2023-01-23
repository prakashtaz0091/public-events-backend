from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List Events':'/events/'
    }

    return Response(api_urls)



@api_view(['GET'])
def eventList(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many = True)
    return Response(serializer.data)