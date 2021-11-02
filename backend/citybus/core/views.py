from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core import serializers
from .models import Album, Route, RouteDetails, TimeSlot
from django.db.models import Q
from rest_framework import status,viewsets
from .serializers import AlbumSerializer, RouteSerializer, TimeSlotSerializer,RouteDetailsSerializer
from geopy import distance

# Create your views here.

@api_view(['GET'])
def home(request,**kwargs):
    if request.method == 'GET':
        album = Album.objects.all()
        print(kwargs)
        serializer_context = {
            'request': request,
        }
        serializers = AlbumSerializer(album,many=True, context=serializer_context)
    return Response(serializers.data)

@api_view(['POST'])
def pickup(request):

    location = request.data['pickup']
    print(location)
    try:
        result = TimeSlot.objects.filter(

            Q(bus_at_now__name__icontains = location) & Q(station_serial__exact=1)).distinct()[:3]
        print(result)
        serializers = TimeSlotSerializer(result,many=True)
        return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)
    except TimeSlot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def destination(request):
    bus_id = request.data['bus_id']
    serial_number = int(request.data['serial_number'])
    trip_number = request.data['trip_number']

    
    try:
        obj = TimeSlot.objects.filter(
            Q(bus_name__id__exact=bus_id) & Q(station_serial__gt=serial_number) &  Q(trip_number__exact = trip_number)
            #Q(bus_at_now__id = bus_id) and Q(station_serial__gt=2) and Q(trip_number__exact = trip_number)
        ).order_by('station_serial')
        
        serializers = TimeSlotSerializer(obj,many=True)
        return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)

        
    except TimeSlot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def check(request):
    pickup_longitude = request.GET.get('pickup_longitude',None)
    pickup_latitude = request.GET.get('pickup_latitude',None)
    destination_longitude = request.GET.get('destinantion_longitude',None)
    destination_latitude = request.GET.get('destinantion_latitude',None)

    pickup = (pickup_longitude,pickup_latitude)
    destination = (destination_longitude,destination_latitude)

    km = int(distance.distance(pickup,destination).km)/10000

    return JsonResponse({
        'distance':km
    })

@api_view(['GET'])
def route_details(request):
    obj = RouteDetails.objects.all()
    serializers = RouteDetailsSerializer(obj,many=True)
    return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)
        


