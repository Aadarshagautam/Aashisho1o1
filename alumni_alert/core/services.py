from django.contrib.gis.measure import D
from django.core.mail import send_mail
from django.conf import settings
from .models import Alumni, DisasterAlert

def find_affected_alumni(disaster):
    radius = D(km=100)
    return Alumni.ojects.fileter(location_distance_lte=(disaster.lcation, radius))

def send_alert_email(alumni, disaster):
    subject = f'Alert: {disaster.title} near your location'
    message = f'''
    Dear {alumni.name},

    A {disaster.get_severity_display()} severity disaster has been reported near your location:

    {disaster.description}

    Please stay safe and follow instructions from local authorities.

    Best regards,
    Alumni Alert System
    '''
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [alumni.email])