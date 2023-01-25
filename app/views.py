from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event

from datetime import date

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List Events':'/events/'
    }

    return Response(api_urls)


def serialize(dbResult,many):
    serializer = EventSerializer(dbResult, many = many)

    return serializer.data
    

def finalizeData(events,dbEvents):
    if len(events)==len(dbEvents):
            for i in range(len(events)):
                if date.today()>dbEvents[i].date:
                    events[i]['missed']=True
                else:
                    events[i]['missed']=False


    return events

@api_view(['GET'])
def eventList(request):
    dbEvents = Event.objects.all()

    events = serialize(dbEvents,True)

    finalData = finalizeData(events,dbEvents)
  
    return Response(finalData)




# filter by district
@api_view(['GET'])
def filterByDistrict(request,district):

    dbEvents = Event.objects.filter(district__icontains=district)

    events = serialize(dbEvents,True)

    finalData = finalizeData(events,dbEvents)

    return Response(finalData)


# filter by municipality
@api_view(['GET'])
def filterByMunicipality(request,municipality):

    dbEvents = Event.objects.filter(municipality__icontains=municipality)
    events = serialize(dbEvents,True)

    finalData = finalizeData(events,dbEvents)
    return Response(finalData)



# filter by local address
@api_view(['GET'])
def filterByLocalAddress(request,local_address):

    dbEvents = Event.objects.filter(localAddress__icontains=local_address)
    events = serialize(dbEvents,True)

    finalData = finalizeData(events,dbEvents)
    return Response(finalData)
