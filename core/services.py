import requests
import xml.etree.ElementTree as ET
from django.contrib.gis.measure import D
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.contrib.gis.geos import Point
from .models import Alumni, DisasterAlert

def fetch_disasters():
    url = "https://www.gdacs.org/xml/rss.xml"
    response = requests.get(url)
    root = ET.fromstring(response.content)

    for item in root.findall('.//item'):
        title = item.find('title').text
        description = item.find('description').text
        lat = float(item.find('geo:lat', {'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#'}).text)
        lon = float(item.find('geo:long', {'geo': 'http://www.w3.org/2003/01/geo/wgs84_pos#'}).text)
        
        DisasterAlert.objects.create(
            title=title,
            description=description,
            location=Point(lon, lat),
            severity=calculate_severity(title),
            created_at=timezone.now()
        )

def calculate_severity(title):
    if "Red Alert" in title:
        return 4  # Critical
    elif "Orange Alert" in title:
        return 3  # High
    elif "Green Alert" in title:
        return 1  # Low
    else:
        return 2  # Medium

def check_disasters():
    recent_disasters = DisasterAlert.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=1))
    for disaster in recent_disasters:
        affected_alumni = find_affected_alumni(disaster)
        for alumnus in affected_alumni:
            send_alert_email(alumnus, disaster)

def find_affected_alumni(disaster):
    radius = D(km=100)
    return Alumni.objects.filter(location__distance_lte=(disaster.location, radius))

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

    # Also notify the supervisor
    supervisor_subject = f"Disaster Alert: {disaster.title} - Affected Alumni Notified"
    supervisor_message = f"A disaster alert has been sent to {alumni.name} ({alumni.email}) regarding {disaster.title}."
    supervisor_email = "supervisor@example.com"  # Replace with actual supervisor email
    send_mail(supervisor_subject, supervisor_message, settings.DEFAULT_FROM_EMAIL, [supervisor_email])