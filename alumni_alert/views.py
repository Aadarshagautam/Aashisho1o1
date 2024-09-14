from django.shortcuts import render
from .models import DisasterAlert

def alerts_list(request):
    alerts = DisasterAlert.objects.all()
    return render(request, 'alerts/alerts_list.html', {'alerts': alerts})
