from django.contrib.gis.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator

class Alumni(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique =True)
    city = models.CharField(max_length=100, blank = True)
    country = models.CharField(max_length=100, blank = True)
    location = models.PointField()
    # longitude = models.PointField()
    graduation_year = models.IntegerField()

    def __str__(self):
        return self.name
    
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
    #longitude = models.PointField()
    severity = models.IntegerField(choices=SEVERITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - Severity: {self.get_severity_display()}"
    
