from django.db import models
from django.utils.timezone import now

class Event(models.Model):
    title = models.CharField(max_length = 150)
    district = models.CharField(max_length = 200)
    municipality = models.CharField(max_length = 200)
    localAddress = models.CharField(max_length = 200)
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    
    
    exactLocation = models.CharField(max_length = 1000)
    details = models.TextField(blank=True)
    

    def __str__(self):
        return self.title

    
    
    
    
    
