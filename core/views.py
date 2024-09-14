from django.shortcuts import render
from django.contrib.gis.measure import D
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Alumni, DisasterAlert
from .serializers import AlumniSerializer, DisasterAlertSerializer

class AlumniViewSet(viewsets.ModelViewSet):
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer

class DisasterAlertViewSet(viewsets.ModelViewSet):
    queryset = DisasterAlert.objects.all()
    serializer_class = DisasterAlertSerializer

    @action(detail=True, methods=['get'])
    def affected_alumni(self, request, pk=None):
        disaster = self.get_object()
        affected_alumni = Alumni.objects.filter(
            location__distance_lte=(disaster.location, D(km=100))
        )
        serializer = AlumniSerializer(affected_alumni, many=True)
        return Response(serializer.data)

def home(request):
    alumni_count = Alumni.objects.count()
    disaster_count = DisasterAlert.objects.count()
    return render(request, 'core/home.html', {
        'alumni_count': alumni_count,
        'disaster_count': disaster_count
    })