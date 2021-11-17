from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser

from core import serializers
from .models import Album, Route, RouteDetails, Ticket, TimeSlot
from django.db.models import Q
from rest_framework import status,viewsets
from .serializers import AlbumSerializer, ApplyHalfSerializer, FileSerializer, RouteSerializer, TicketSerializer, TimeSlotSerializer,RouteDetailsSerializer
from geopy import distance
import datetime

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
    
    print(now)
    serializers = RouteDetailsSerializer(obj,many=True)
    return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def route_name(request):
    obj = Route.objects.all().order_by('name')
    
    serializers = RouteSerializer(obj,many=True)
    return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT'])
def ticket(request):

    if request.method == 'GET':
        user_id = request.user.id
        
        obj = Ticket.objects.filter(user__id__exact = user_id )
        if obj:
            serializers = TicketSerializer(obj,many=True)
            return Response({"status": "success", "data":serializers.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "success", "data":"There is no ticket yet"}, status=status.HTTP_200_OK)
    if request.method == 'POST':
        # now = datetime.datetime.now().strftime('%I:%M %p')
        user_id = request.user.id
        pickup = request.data['pickup']
        destination = request.data['destination']
        time = request.data['time']
        
        # print(now>time)

        data = {
            'user':user_id,
            'pickup':pickup,
            'destination':destination,
            'time':time
        }
        

        serializers = TicketSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        now = datetime.datetime.now().strftime('%I:%M %p')
        ticket_id = request.data['id']
        time = request.data['time']
        obj = Ticket.objects.get(id=ticket_id)
        if request.user.is_authenticated:
            obj.delete()
            return Response("ok_clear", status=status.HTTP_200_OK)
        else:
            return Response("you have to be logged in ", status=status.HTTP_200_OK)


class FileUpload(APIView):
    parser_class = (FileUploadParser,)
    def post(self,request,*args,**kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def apply_half(request):
    if request.method == 'POST':
        serializer = ApplyHalfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




        








    




        


