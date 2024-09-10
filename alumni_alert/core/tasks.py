from celery import shared_task
from .services import find_affected_alumni, send_alert_email
from .models import DisasterAlert

@shared_task
def process_disaster_alert(disaster_id):
    try:
        disaster = DisasterAlert.objects.get(id=disaster_id)
        affected_alumni = find_affected_alumni(disaster)
        for alumnus in affected_alumni:
            send_alert_email(alumnus, disaster)
    
    except DisasterAlert.DoesNotExist:
        pass