from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Room(models.Model):
    number = models.CharField(max_length=50)
    capacity = models.IntegerField()
    description = models.TextField(default='')

    def __str__(self):
        return f"Room #{self.number} - {self.capacity}"
    
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        #ordering = ["number"]


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="booked")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booked")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.room}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["start_time"]

