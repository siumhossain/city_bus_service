from django.urls import path
from .import views
urlpatterns = [
   path('',views.home),
   path('route_search/',views.pickup),
   path('route_search_destination/',views.destination),
   path('route_details/',views.route_details),
   path('route_name/',views.route_name),
   
   path('check/',views.check),

]