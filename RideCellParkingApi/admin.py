from django.contrib import admin
from RideCellParkingApi.models import Places, AllParkingSpots, AvailableParkingSpots, ReservedParkingSpots

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('lat', 'lng')

class AllParkingSpotAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'lat', 'lng')

class AvailableParkingSpotsAdmin(admin.ModelAdmin):
    list_display = ('parking_id', 'place_id', 'distance')

class ReservedParkingSpotsAdmin(admin.ModelAdmin):
    list_display = ('parking_id', 'time_range')


admin.site.register(Places, PlacesAdmin)
admin.site.register(AllParkingSpots, AllParkingSpotAdmin)
admin.site.register(AvailableParkingSpots, AvailableParkingSpotsAdmin)
admin.site.register(ReservedParkingSpots, ReservedParkingSpotsAdmin)
