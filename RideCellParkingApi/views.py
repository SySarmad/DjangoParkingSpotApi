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

def add_parking_spots_to_place(place_id, parkingspot_id, distance):
    """Adds a parking Spot to the table"""
    new_parking_spot = AvailableParkingSpots(p_id=parkingspot_id, place_id=place_id, distance=distance)
    new_parking_spot.save()

def add_place(lat, lng):
    places = Places(lat=lat, lng=lng)
    places.save()
    p_id = Places.objects.get(lat=lat, lng=lng).id
    return p_id

def find_and_add_all_parking_spots(place_id, lat, lng, radius):
    """This finds all parking spots within r and adds it to the list"""
    all_spots = AllParkingSpots.objects.all()
    for i in all_spots:
        if haversine(lat, lng, i[1], i[2]) <= radius:
            new_spot = AvailableParkingSpots(parking_id=i.id, place_id=place_id, distance=radius)


def get_all_available_parking_spots(lat, lng, radius):
    p_id = add_place(lat, lng)
    available_parking_spots = AvailableParkingSpots.objects.filter(place_id=p_id, distance_lte=radius)

    if len(available_parking_spots) == 0:
        find_and_add_all_parking_spots(p_id, lat, lng, radius)
    return available_parking_spots
