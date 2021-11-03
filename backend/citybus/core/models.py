from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from geopy.geocoders import Nominatim
from django.db.models import Q
geolocator = Nominatim(user_agent="city_bus")
# Create your models here.
class User(AbstractUser):
    pass 

class BusCompany(models.Model):
    company_name = models.CharField(max_length=30)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,default='')
    market_value = models.FloatField(null=True,blank=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.company_name


    
class Route(models.Model):
    name = models.CharField(max_length=300,blank=True,editable=False)
    longitude = models.CharField(max_length=50,null=True,blank=True)
    latitude = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return f'{self.id} | {self.name}|{self.latitude}|{self.latitude}'

    def save(self,*args,**kwargs):
        location = geolocator.reverse(f'{self.longitude},{self.latitude}',language='en')
        
        self.name = location.address
        super().save(*args,**kwargs)

class Bus(models.Model):
    name = models.CharField(max_length=30)
    available_seat = models.IntegerField(default=0)
    seat_each_row = models.IntegerField(default=0)
    description = models.TextField(blank=True,null=True)
    owner = models.ForeignKey('BusCompany',on_delete=models.CASCADE)
    stuff = models.ManyToManyField(User)
    license_number = models.CharField(max_length=30,unique=True)


    def __str__(self):
        return self.name




class TimeSlot(models.Model):
    bus_name = models.ForeignKey('Bus',on_delete=models.CASCADE,related_name='bus_name')
    bus_at_now = models.ForeignKey('Route',on_delete=models.CASCADE,related_name='route_name')
    station_serial = models.IntegerField()
    trip_number = models.IntegerField()
    time = models.TimeField()

    class Meta:
        ordering = ['bus_name','trip_number','station_serial','time']

    def save(self,*args,**kwargs):
        
        check = TimeSlot.objects.filter(
            Q(bus_name__name__exact = self.bus_name) & Q(time__exact = self.time) 
        )
        if check:
            print('wrong')
        else:        
            super().save(*args,**kwargs)
    def __str__(self):
        return f'{self.bus_name} | station serial:{self.station_serial} | trip_number {self.trip_number} |{self.time} |  {self.bus_at_now}'
            

        
        
        
       

class Ticket(models.Model):
    buyer = models.ForeignKey('User',on_delete=models.CASCADE)
    bus = models.ForeignKey('Bus',on_delete=models.CASCADE)
    deprature_point = models.CharField(max_length=50,default='')
    destination = models.CharField(max_length=50,default='')
    seat_number = models.CharField(max_length=10,default='')
    validity = models.BooleanField(default=True)
    price = models.FloatField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.buyer} | {self.bus}'





class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return f'{self.order} : {self.title}'


class RouteDetails(models.Model):
    route = models.ManyToManyField(TimeSlot)