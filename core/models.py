from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Alumni(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    location = models.PointField()  # This will store both latitude and longitude
    graduation_year = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.location:
            self.location = Point(0.0, 0.0)  # Default to (0, 0) if no location is provided
        super().save(*args, **kwargs)

    @property
    def latitude(self):
        return self.location.y if self.location else None

    @property
    def longitude(self):
        return self.location.x if self.location else None

class DisasterAlert(models.Model):
    SEVERITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
        (4, 'Critical'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.PointField()
    severity = models.IntegerField(choices=SEVERITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - Severity: {self.get_severity_display()}"

    @property
    def latitude(self):
        return self.location.y if self.location else None

    @property
    def longitude(self):
        return self.location.x if self.location else None