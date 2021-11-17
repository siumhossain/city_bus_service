from django.contrib import admin


from .models import Album, ApplyHalf, BusCompany, Bus, Fileup, Route, RouteDetails, Ticket, TimeSlot, Track, User  
# Register your models here.


admin.site.register(User)
admin.site.register(BusCompany)
admin.site.register(Route)



admin.site.register(Bus)
admin.site.register(Ticket)
admin.site.register(TimeSlot)
admin.site.register(RouteDetails)
admin.site.register(Fileup)
admin.site.register(ApplyHalf)











