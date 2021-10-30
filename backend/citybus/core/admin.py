from django.contrib import admin


from .models import Album, BusCompany, Bus, Route,Ticket, TimeSlot, Track, User  
# Register your models here.


admin.site.register(User)
admin.site.register(BusCompany)
admin.site.register(Route)


admin.site.register(Ticket)
admin.site.register(Bus)
admin.site.register(TimeSlot)









