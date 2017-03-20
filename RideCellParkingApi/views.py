from django.shortcuts import render_to_response, get_object_or_404
from RideCellParkingApi.models import Places, AllParkingSpots, AvailableParkingSpots, ReservedParkingSpots
from math import radians, cos, sin, asin, sqrt



def haversine(lon1, lat1, lon2, lat2):
    """
    Not Mine algorithm From Stack Overflow, and really all over the place this was most optimized
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def add_parking_spots(place_id, parkingspot_id, distance):
    new_parking_spot = AvailableParkingSpots(p_id=parkingspot_id, place_id=place_id, distance=distance)



def get_all_available_parking_spots(lat, lng, radius):
    places = Places(lat=lat, lng=lng).save()
    p_id = Places.objects.get(lat=lat, lng=lng).id
    available_parking_spots = AvailableParkingSpots.objects.filter(distance_lte=radius)
    return available_parking_spots
