from django.db import models


class Places(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)

    def __str__(self):
        return "{}, {}".format(self.lat, self.lng)

class AllParkingSpots(models.Model):
    p_id = models.SlugField(max_length=6, primary_key=True, null=False)
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    lng = models.DecimalField(max_digits=11, decimal_places=8)

    def __str__(self):
        return "{}, {}, {}".format(self.p_id, self.lat, self.lng)


class AvailableParkingSpots(models.Model):
    parking_id = models.ForeignKey(AllParkingSpots)
    place_id = models.ForeignKey(Places)
    radius = models.IntegerField(max_length=10, null=False)

    def __str__(self):
        return "{}, {}, {}".format(self.parking_id, self.place_id, self.radius)

class ReservedParkingSpots(models.Model):
    parking_id = models.OneToOneField(AvailableParkingSpots)
    time_range = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return "{}, {}".format(self.parking_id, self.time_range)